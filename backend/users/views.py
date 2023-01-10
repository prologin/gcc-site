from rest_framework import generics, permissions, viewsets
from django_filters import rest_framework as filters
from gccsite.serializers import MultipleSerializerViewSetMixin

from . import models, serializers

class UserFilter(filters.FilterSet):
    email = filters.CharFilter(
        help_text = "Get user by email"
    )

    class Meta:
        model = models.User
        fields = []

class UserViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.UserSerializer
    filterset_class = UserFilter

    def get_queryset(self):
        return models.User.objects.filter()


class UserMeView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
