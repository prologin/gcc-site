from rest_framework import serializers

from . import models


class PartnerShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = (
            "id",
            "name",
            "logo",
            "order",
        )


class PartnerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = (
            "name",
            "description",
            "website_url",
            "logo",
        )


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = "__all__"
