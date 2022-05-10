from rest_framework import permissions, viewsets

from .. import models, serializers


class FormViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer


class ApplicationViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ApplicationSerializer
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        return models.Application.objects.filter(
            user=self.request.user,
        )
