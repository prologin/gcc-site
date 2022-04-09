from rest_framework import viewsets
from . import models, serializers


class PartnerViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.PartnerSerializer

    def get_queryset(self):
        return models.Partner.objects.filter(enabled=True)
