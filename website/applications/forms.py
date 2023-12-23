import re
from typing import Optional

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    Button,
    Column,
    Div,
    Field,
    Layout,
    Row,
    Submit,
)
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.core.validators import validate_email
from django.db import models
from django.http import QueryDict
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from applications.models import Application
from profiles.models import Profile

SCHOOL_LEVEL = [
    (None, "-"),  # Start choice
    ("6ème", "6ème"),
    ("5ème", "5ème"),
    ("4ème", "4ème"),
    ("3ème", "3ème"),
    ("Seconde", "Seconde"),
    ("Première", "Première"),
    ("Terminale", "Terminale"),
]

TSHIRT = [
    (None, "-"),
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("XXL", "XXL"),
]

# Must be the same as static/js/forms/form.js:PHONE_REGEX
PHONE_REGEX = r"^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$"


class EventApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["event", "profile", "form_answer"]
        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": _(
                    "Une candidature avec ce profil est déjà enregistrée pour ce stage"
                ),
            }
        }

    profile = forms.TypedChoiceField(
        label="Sélectionner mon profil participante",
        choices=[],
        empty_value=None,
        coerce=lambda id: Profile.objects.get(id=id),
        required=True,
    )

    # Info supplémentaires sur la participante (en + du profil)
    school_level = forms.ChoiceField(
        label="Niveau d'études", choices=SCHOOL_LEVEL
    )

    allergies = forms.CharField(
        label="La participante a-t-elle des allergies ?",
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
    )

    diet = forms.CharField(
        label="La participante a-t-elle un régime alimentaire particulier ?",
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
    )

    tshirt = forms.ChoiceField(
        label="Quelle est la taille de t-shirt de la participante ?",
        choices=TSHIRT,
        help_text="Un t-shirt sera donné aux participantes pendant le stage",
    )

    learn = forms.CharField(
        label="Y a-t'il quelque chose en particulier que la participante espère apprendre pendant le stage ?",
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
    )

    programing = forms.CharField(
        label="La participante a-t-elle déjà programmé ? Si oui, quand a-t-elle codé pour la première fois et quels outils ou langages de programmation a-t-elle essayées ?",
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
    )

    studies = forms.CharField(
        label="Y a-t-il des études en informatique qui intéresseraient la participante ? Si oui, pourrait-elle préciser lesquelles ?",
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
    )

    association = forms.CharField(
        label="Par quel moyen a-t-elle connu l'association et les stages ?",
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
    )

    def __init__(self, *args, **kwargs):
        if "profile_qs" in kwargs:
            choices = [(None, "-")]
            qs = kwargs.pop("profile_qs")
            choices.extend(
                [
                    (entry.id, f"{entry.first_name} {entry.last_name}")
                    for entry in qs
                ]
            )
            self.base_fields["profile"].choices = choices

        if len(args) > 0 and isinstance(args[0], QueryDict):
            # If POSTing, add a form_answer value to the input which is
            # aggregated from the other fields
            query_dict = args[0].copy()  # Copy beacuse it is read only
            query_dict.update(
                {
                    "form_answer": {
                        "school_level": query_dict.get("school_level"),
                        "tshirt": query_dict.get("tshirt"),
                        "allergies": query_dict.get("allergies"),
                        "diet": query_dict.get("diet"),
                        "learning": query_dict.get("learn"),
                        "programing": query_dict.get("programing"),
                        "studies": query_dict.get("studies"),
                        "association": query_dict.get("association"),
                    }
                }
            )
            args = (query_dict,) + args[1:]
            super().__init__(*args, **kwargs)
        else:
            super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_id = "application_form"
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Div(
                Row(
                    Column(
                        Button(
                            name="next",
                            value="J'ai déjà un profil",
                            css_class="my-4 btn btn-primary btn-block",
                        ),
                    ),
                    Column(
                        Button(
                            name="next",
                            value="Je crée un profil",
                            css_class="my-4 btn btn-primary btn-block",
                        ),
                    ),
                    css_class="mt-4 p-0",
                ),
                css_class="tab active",
            ),
            Div(
                Field("profile"),
                Field("school_level"),
                Div(
                    Row(
                        Column(
                            Button(
                                name="back",
                                value="Retour",
                                css_class="my-4 btn btn-light btn-block",
                            )
                        ),
                        Column(
                            Submit(
                                name="next",
                                value="Suivant",
                                css_class="my-4 btn btn-primary btn-block",
                            )
                        ),
                    ),
                    css_class="mt-4 p-0",
                ),
                css_class="tab active",
            ),
            Div(
                Field("tshirt"),
                Field("allergies"),
                Field("diet"),
                Field("learn"),
                Field("programing"),
                Field("studies"),
                Field("association"),
                Div(
                    Row(
                        Column(
                            Button(
                                name="back",
                                value="Retour",
                                css_class="my-4 btn btn-light btn-block",
                            )
                        ),
                        Column(
                            Submit(
                                name="submit-application",
                                value="Candidater pour ce stage",
                                css_class="my-4 btn btn-primary btn-block",
                            )
                        ),
                    ),
                    css_class="mt-4 p-0",
                ),
                css_class="tab",
            ),
        )
