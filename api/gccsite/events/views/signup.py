from django_filters import rest_framework as filters
from gccsite.serializers import MultipleSerializerViewSetMixin
from rest_framework import permissions, viewsets

from .. import models, serializers


class FormViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer


class ApplicationFilter(filters.FilterSet):
    user_id = filters.NumberFilter(field_name="user__id")
    event_id = filters.NumberFilter(field_name="event__id")

    class Meta:
        model = models.Application
        fields = ["user_id", "event_id", "status"]


class ApplicationViewset(
    MultipleSerializerViewSetMixin, viewsets.ModelViewSet
):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.ApplicationSerializer
    actions_serializer_classes = {
        "list": serializers.ApplicationShortSerializer
    }

    http_method_names = ["get", "post", "delete"]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ApplicationFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Application.objects
        else:
            return models.Application.objects.filter(user=self.request.user)
