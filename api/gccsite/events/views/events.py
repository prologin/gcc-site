from rest_framework import permissions, response, viewsets
from rest_framework.decorators import action

from .. import models, serializers


class EventViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.get_visible_events()

    @action(detail=False, methods=["get"], url_path="open")
    def open_events(self, request):
        objects = models.Event.objects.get_open_events()
        serializer = self.get_serializer_class()
        return response.Response(serializer(objects, many=True).data)
