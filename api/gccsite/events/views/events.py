"""
This view is an endpoint for the list of events, which can be filtered using
query parameters.

Parameters
----------

- `only_open`: Only return the list of events whose registrations are still
  open
- `center`: Filter by exact match from center name
- `starts_after`: Only return events that start after the given date
- `ends_before`: Only return events that ends before the given date
- `signup_starts_after`: Only return events whose registrations start after
  the given date
- `signup_ends_before`: Only return events whose registrations ends before
  the given date

Examples
--------

- `/api/events?only_open=true`
- `/api/events?starts_after=2022-04-04&ends_before=2022-04-15`
"""

from django.utils import timezone
from django_filters import rest_framework as filters
from django_filters.compat import coreschema
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, response, viewsets
from rest_framework.decorators import action

from .. import models, serializers


def filter_open(queryset, name, value):
    if value:
        return queryset.filter(
            signup_start_date__lte=timezone.now(),
            signup_end_date__gt=timezone.now(),
        )
    return queryset


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


class EventFilter(filters.FilterSet):
    only_open = filters.BooleanFilter(method=filter_open)
    center = filters.CharFilter(field_name="center__name")
    starts_after = filters.DateFilter(
        field_name="start_date", lookup_expr="gte"
    )
    ends_before = filters.DateFilter(field_name="end_date", lookup_expr="lte")
    signup_starts_after = filters.DateFilter(
        field_name="signup_start_date", lookup_expr="gte"
    )
    signup_ends_before = filters.DateFilter(
        field_name="signup_end_date", lookup_expr="lte"
    )

    class Meta:
        model = models.Event
        fields = []


class EventViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects
    filterset_class = EventFilter

    @action(methods=["get"], detail=True)
    @swagger_auto_schema(
        responses={200: serializers.QuestionSerializer(many=True)}
    )
    def questions(self, request, pk):
        event = self.get_object()
        serializer = serializers.QuestionSerializer(
            models.Form.objects.get(id=event.form.id).questions,
            many=True,
        )
        return response.Response(serializer.data)
