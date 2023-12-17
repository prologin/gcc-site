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
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from applications.models import Application

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


def phoneNumberTest(phone):
    if re.match(PHONE_REGEX, str(phone)):
        raise ValidationError("Not a phone number")


class EventApplicationForm(forms.Form):
    profile = forms.ChoiceField(label="Profil de la participante", choices=[])

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
        if "profile_choices" in kwargs:
            self.base_fields["profile"].choices = kwargs.pop("profile_choices")
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "application_form"
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Div(
                Field("profile"),
                Field("school_level"),
                Div(
                    Button(
                        name="next",
                        value="Suivant",
                        css_class="my-4 btn btn-primary btn-block",
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

    def clean_form_answers(self) -> Optional[dict]:
        if not self.is_valid():
            return None
        return {
            "tshirt": self.cleaned_data["tshirt"],
            "allergies": self.cleaned_data["allergies"],
            "diet": self.cleaned_data["diet"],
            "learning": self.cleaned_data["learn"],
            "programing": self.cleaned_data["programing"],
            "studies": self.cleaned_data["studies"],
            "association": self.cleaned_data["association"],
        }
