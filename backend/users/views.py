from rest_framework import generics, permissions, viewsets

from gccsite.serializers import MultipleSerializerViewSetMixin

from . import models, serializers

class UserViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.UserSerializer


class UserMeView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user
