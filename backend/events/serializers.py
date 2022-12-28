from collections import defaultdict, deque

import jsonschema
from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
            "id",
            "street",
            "complement",
            "zip_code",
            "city",
            "country",
            "lat",
            "lng",
        )


class CenterSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = models.Center

        fields = (
            "id",
            "name",
            "address",
        )


class EventSerializer(serializers.ModelSerializer):
    center = CenterSerializer()

    class Meta:
        model = models.Event
        depth = 1

        fields = (
            "id",
            "name",
            "camps_type",
            "center",
            "signup_start_date",
            "signup_end_date",
            "start_date",
            "end_date",
            "form_id",
            "description",
            "notes",
        )


class PartialEventSerializer(serializers.ModelSerializer):
    center = serializers.CharField(source="center.name")

    class Meta:
        depth = 1
        model = models.Event
        fields = (
            "id",
            "name",
            "center",
            "start_date",
            "end_date",
        )


class EventShortSerializer(serializers.ModelSerializer):
    center_name = serializers.CharField(source="center.name")

    class Meta:
        model = models.Event
        depth = 0

        fields = (
            "id",
            "center_name",
            "start_date",
            "end_date",
        )


class EventDocumentSerializer(serializers.ModelSerializer):
    file = serializers.ReadOnlyField(source="document.file.url")

    class Meta:
        model = models.EventDocument

        fields = (
            "file",
            "display_name",
        )


class FormShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Form

        fields = ("id", "name")


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Form

        fields = (
            "id",
            "name",
            "json_schema",
            "ui_schema",
        )


class ApplicationValidator:
    requires_context = True

    @staticmethod
    def rec_defaultdict():
        """Recursive defaultdict"""
        return defaultdict(ApplicationValidator.rec_defaultdict)

    @staticmethod
    def add_error(errors, keys_dq, err):
        """Adds an error to the error dict

        Args:
            errors (dict): errors dictionary
            keys_dq (deque): keys deque
            err (str): error to add

        Returns:
            dict: errors dictionary updated
        """
        k = keys_dq.popleft()

        if len(keys_dq) == 0:
            if errors[k]:
                if isinstance(errors[k], list):
                    errors[k].append(err)
                else:
                    errors[k] = [errors[k], err]
            else:
                errors[k] = err
        else:
            errors[k] = ApplicationValidator.add_error(errors[k], keys_dq, err)

        return errors

    def __call__(self, value, serializer):
        event = models.Event.objects.get(
            pk=value["event"].id
            if value.get("event")
            else serializer.instance.event_id
        )

        # Event validation
        if not event.is_open:
            raise serializers.ValidationError(
                {"event": "Cet évènement n'accepte pas les inscriptions."}
            )

        answer = value.get("form_answer")
        # # Validate answer if it has been changed
        # # OR if the Application is created (POST) or updated (PUT)
        # # meaning that partial is False
        if answer or not serializer._kwargs.get("partial", False):
            validator = jsonschema.Draft202012Validator(event.form.json_schema)

            errors = ApplicationValidator.rec_defaultdict()
            for err in validator.iter_errors(answer):
                ApplicationValidator.add_error(
                    errors,
                    # If there is no relative_path, the error is that the
                    # argument is required
                    err.relative_path or deque(["required"]),
                    err.message,
                )

            if errors:
                raise serializers.ValidationError({"form_answer": errors})


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    form_answer = serializers.JSONField(required=True)

    class Meta:
        model = models.Application
        fields = (
            "id",
            "user",
            "event",
            "first_name",
            "last_name",
            "dob",
            "status",
            "form_answer",
        )

        read_only_fields = ("id", "user", "status")

        validators = [ApplicationValidator()]

    def create(self, validated_data):
        request = self.context["request"]

        validated_data["user"] = request.user
        validated_data["status"] = models.SelectionStatus.ENROLLED.value

        return super().create(validated_data)


class ApplicationShortSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    event = EventShortSerializer()

    class Meta:
        model = models.Application
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "event",
            "status",
        )

        read_only_fields = ("id", "user", "status")


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = ("id", "status")

        read_only_fields = ("id",)
