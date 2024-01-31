from rest_framework import serializers

from applications.models import Application


class ApplicationExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "tshirt",
            "first_name_resp",
            "last_name_resp",
            "phone_resp",
            "email_resp",
        ]
        read_only_fields = fields

    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.profile.user.get_username()
