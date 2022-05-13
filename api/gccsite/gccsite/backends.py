from django_filters import rest_framework as filters
from drf_yasg import openapi
from rest_framework.compat import coreschema


class FilterBackend(filters.DjangoFilterBackend):
    """
    The default filter backend does not properly set the field types,
    making all query parameters string type.

    This is a simple override that supports boolean and date filters.
    """

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
