from django_filters import rest_framework as filters
from drf_yasg import openapi
from rest_framework.compat import coreschema


class FilterBackend(filters.DjangoFilterBackend):
    """
    Simple filter that supports number, boolean, date and datetime types.

    It also adds `help_text` and `choices` values to the Field description to
    improve API documentation.
    """

    def get_coreschema_field(self, field):
        format_ = None
        field_cls = coreschema.String

        description_parts = []

        if help_text := field.extra.get("help_text", ""):
            description_parts.append(help_text)

        if isinstance(field, filters.NumberFilter):
            field_cls = coreschema.Number
        elif isinstance(field, filters.BooleanFilter):
            field_cls = coreschema.Boolean
        elif isinstance(field, filters.DateFilter):
            format_ = openapi.FORMAT_DATE
        elif isinstance(field, filters.DateTimeFilter):
            format_ = openapi.FORMAT_DATETIME
        elif isinstance(field, filters.ChoiceFilter):
            choices = list(
                map(lambda choice: choice[0], field.extra.get("choices", []))
            )
            if choices:
                description_parts.append(f"Value must be in `{choices}`.")

        field = field_cls(description=" ".join(description_parts))
        field.format = format_

        return field
