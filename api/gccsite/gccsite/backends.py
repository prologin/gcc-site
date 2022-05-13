from django_filters import rest_framework as filters
from drf_yasg import openapi
from rest_framework.compat import coreschema


class FilterBackend(filters.DjangoFilterBackend):
    def get_coreschema_field(self, field):
        format = None
        field_cls = coreschema.String
        if isinstance(field, filters.NumberFilter):
            field_cls = coreschema.Number
        elif isinstance(field, filters.BooleanFilter):
            field_cls = coreschema.Boolean
        elif isinstance(field, filters.DateFilter):
            format = openapi.FORMAT_DATE
        elif isinstance(field, filters.DateTimeFilter):
            format = openapi.FORMAT_DATETIME
        field = field_cls(description=str(field.extra.get("help_text", "")))
        field.format = format
        return field
