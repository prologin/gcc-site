from rest_framework import permissions, viewsets

from .. import models, serializers


class AttendeeViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AttendeeSerializer
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        return models.Attendee.objects.filter(
            owner=self.request.user,
        )
