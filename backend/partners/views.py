from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets

from . import models, serializers


class PartnerFilter(filters.FilterSet):
    is_on_front_page = filters.BooleanFilter(
        help_text=(
            "If `true`, only returns partners that should be displayed on the"
            " front page."
        )
    )
    featured = filters.BooleanFilter(
        help_text="If `true`, only returns partners that should be featured."
    )

    class Meta:
        model = models.Partner
        fields = []


class PartnerViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    filterset_class = PartnerFilter

    serializer_class = serializers.PartnerSerializer

    def get_queryset(self):
        return models.Partner.objects.filter(enabled=True)
