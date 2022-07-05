from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
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


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question

        fields = (
            "id",
            "order",
            "text",
            "type",
            "mandatory",
            "possible_answers",
        )


class EventDocumentSerializer(serializers.ModelSerializer):
    file = serializers.ReadOnlyField(source="document.file.url")

    class Meta:
        model = models.EventDocument

        fields = (
            "file",
            "display_name",
        )


class FormSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = models.Form

        fields = (
            "id",
            "questions",
        )


class FormAnswerValidator:
    def __call__(self, value):
        question, answers = value["question"], value["answer"].splitlines()

        if question.type in (
            models.QuestionType.CHOICE.value,
            models.QuestionType.MULTIPLE_CHOICES.value,
        ):
            possible_answers = question.answers.splitlines()
            for answer in answers:
                if answer not in possible_answers:
                    raise serializers.ValidationError(
                        {
                            "answer": _(
                                f'"{answer}" n\'est pas un choix possible'
                                " (choisir parmi :"
                                f' {", ".join(possible_answers)})'
                            )
                        }
                    )


class FormAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=models.Question.objects.all()
    )

    class Meta:
        model = models.FormAnswer

        fields = (
            "id",
            "question",
            "answer",
        )

        write_only_fields = ("application_id",)
        read_only_fields = ("id",)

        validators = [FormAnswerValidator()]


class ApplicationValidator:
    def __call__(self, value):
        answers = value.get("form_answers", [])
        answers_ids_set = {answer["question"].id for answer in answers}

        event = models.Event.objects.get(pk=value["event"].id)
        questions = event.get_application_questions()

        questions_ids_set = set(questions.values_list("id", flat=True))
        mandatory_questions_ids_set = set(
            questions.filter(mandatory=True).values_list("id", flat=True)
        )

        if len(answers) != len(answers_ids_set):
            raise serializers.ValidationError(
                {
                    "form_answers": _(
                        "Vous avez répondu plusieurs fois à la même question"
                    )
                }
            )

        if answers_ids_set < mandatory_questions_ids_set:
            raise serializers.ValidationError(
                {
                    "form_answers": _(
                        "Certaines questions obligatoires n'ont pas de réponse"
                    )
                }
            )

        if answers_ids_set - questions_ids_set:
            raise serializers.ValidationError(
                {
                    "form_answers": _(
                        "Vous avez répondu à des questions non demandées"
                    )
                }
            )


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    form_answers = FormAnswerSerializer(many=True, required=False)

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
            "form_answers",
        )

        read_only_fields = ("id", "user", "status")

        validators = [ApplicationValidator()]

    def create(self, validated_data):
        request = self.context["request"]

        validated_data["user"] = request.user
        validated_data["status"] = models.SelectionStatus.ENROLLED.value

        try:
            form_answers = validated_data.pop("form_answers")
        except KeyError:
            form_answers = []

        ret = super().create(validated_data)

        for answer in form_answers:
            answer["application_id"] = ret.id
            FormAnswerSerializer().create(answer)

        return ret


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
