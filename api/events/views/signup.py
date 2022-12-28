from django_filters import rest_framework as filters
from rest_framework import permissions, response, status, viewsets
from rest_framework.decorators import action

from gccsite.serializers import MultipleSerializerViewSetMixin

from .. import models, serializers


class FormViewset(
    MultipleSerializerViewSetMixin, viewsets.ReadOnlyModelViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer

    actions_serializer_classes = {
        "list": serializers.FormShortSerializer,
        "read": serializers.FormSerializer,
    }


class ApplicationFilter(filters.FilterSet):
    user_id = filters.NumberFilter(
        field_name="user__id", help_text="Filter by user."
    )
    event_id = filters.NumberFilter(
        field_name="event__id", help_text="Filter by event."
    )
    status = filters.ChoiceFilter(
        help_text="Filter by status.", choices=models.SelectionStatus.choices
    )

    class Meta:
        model = models.Application
        fields = ["user_id", "event_id", "status"]


class ApplicationViewset(
    MultipleSerializerViewSetMixin, viewsets.ModelViewSet
):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.ApplicationSerializer
    actions_serializer_classes = {
        "list": serializers.ApplicationShortSerializer,
        "update_status": serializers.ApplicationStatusSerializer,
    }

    http_method_names = ["get", "post", "delete", "put", "patch"]

    filterset_class = ApplicationFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Application.objects
        else:
            return models.Application.objects.filter(user=self.request.user)

    @action(
        methods=["patch"],
        detail=True,
        permission_classes=[permissions.IsAdminUser],
    )
    def update_status(self, request, pk):
        application = self.get_object()

        serializer = self.get_serializer(
            application, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return response.Response(serializer.data)
        else:
            return response.Response(
                serializer.errors, status.HTTP_400_BAD_REQUEST
            )
