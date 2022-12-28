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

from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, response, viewsets
from rest_framework.decorators import action

from gccsite.serializers import MultipleSerializerViewSetMixin

from .. import models, serializers


class EventFilter(filters.FilterSet):
    only_open = filters.BooleanFilter(
        method="filter_open",
        help_text=(
            "If `true`, only return events for which registrations is open."
        ),
    )
    center = filters.CharFilter(
        field_name="center__name",
        help_text=(
            "Filter by center. "
            "The argument must exactly match the center name."
        ),
    )
    starts_after = filters.DateFilter(
        field_name="start_date",
        lookup_expr="gte",
        help_text="Return events that start after the given date.",
    )
    ends_before = filters.DateFilter(
        field_name="end_date",
        lookup_expr="lte",
        help_text="Return events that end before the given date.",
    )
    signup_starts_after = filters.DateFilter(
        field_name="signup_start_date",
        lookup_expr="gte",
        help_text=(
            "Return events for which registrations "
            "starts after the given date."
        ),
    )
    signup_ends_before = filters.DateFilter(
        field_name="signup_end_date",
        lookup_expr="lte",
        help_text=(
            "Return events for which registrations ends before the given date."
        ),
    )

    class Meta:
        model = models.Event
        fields = []

    def filter_open(self, queryset, name, value):
        if value:
            return models.Event.objects.get_open_events()

        return queryset


class EventViewset(
    MultipleSerializerViewSetMixin, viewsets.ReadOnlyModelViewSet
):
    permission_classes = [permissions.AllowAny]
    queryset = models.Event.objects
    filterset_class = EventFilter

    actions_serializer_classes = {
        "list": serializers.PartialEventSerializer,
        "retrieve": serializers.EventSerializer,
    }

    @action(methods=["get"], detail=True)
    @swagger_auto_schema(responses={200: serializers.FormSerializer()})
    def form(self, request, pk):
        """
        Return the form attached to this event.
        """
        event = self.get_object()
        serializer = serializers.FormSerializer(
            models.Form.objects.get(id=event.form.id),
        )

        return response.Response(serializer.data)

    @action(
        methods=["get"],
        detail=True,
        permission_classes=[permissions.IsAuthenticated],
    )
    @swagger_auto_schema(
        responses={200: serializers.EventDocumentSerializer(many=True)}
    )
    def docs(self, request, pk):
        event = self.get_object()
        try:
            attendee = models.Attendee.objects.get(owner=request.user)
        except models.Attendee.DoesNotExist:
            docs = event.get_attendee_documents(None)
        else:
            docs = event.get_attendee_documents(attendee)
        serializer = serializers.EventDocumentSerializer(docs, many=True)
        return response.Response(serializer.data)
