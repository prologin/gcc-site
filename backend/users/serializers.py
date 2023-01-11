from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    participations_count = serializers.IntegerField()

    class Meta:
        model = models.User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "city",
            "zip_code",
            "country",
            "participations_count",
            "is_staff",
            "user_permissions",
        )

        read_only_fields = (
            "email",
            "is_staff",
        )
