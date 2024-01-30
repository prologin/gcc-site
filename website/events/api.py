import csv

from django.http import HttpResponse
from rest_framework import generics, permissions

from applications.models import Application
from applications.serializers import ApplicationExportSerializer
from events.models import Event


class ExportSelectedApplications(generics.GenericAPIView):
    # TODO: Use correct permission when reworking
    permission_classes = [permissions.IsAdminUser]
    queryset = Event.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="export.csv"'

        event = self.get_object()

        applications = Application.objects.filter(event=event)

        # Only select the application with a requested status
        statuses = request.query_params.get("status")
        if statuses:
            status_list = statuses.split(" ")
            applications = applications.filter(status__in=status_list)

        serializer = ApplicationExportSerializer(applications, many=True)
        header = ApplicationExportSerializer.Meta.fields

        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        for row in serializer.data:
            writer.writerow(row)

        return response
