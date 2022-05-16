from django_filters import rest_framework as filters
from gccsite.serializers import MultipleSerializerViewSetMixin
from rest_framework import permissions, viewsets

from . import models, serializers


class PartnerFilter(filters.FilterSet):
    is_on_front_page = filters.BooleanFilter()
    featured = filters.BooleanFilter()

    class Meta:
        model = models.Partner
        fields = []


class PartnerViewset(
    MultipleSerializerViewSetMixin, viewsets.ReadOnlyModelViewSet
):
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PartnerFilter

    serializer_class = serializers.PartnerSerializer

    actions_serializer_classes = {
        "list": serializers.PartnerShortSerializer,
        "retrieve": serializers.PartnerDetailsSerializer,
    }

    def get_queryset(self):
        return models.Partner.objects.filter(enabled=True)
