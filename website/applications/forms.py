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

NB_PARTICIPATIONS = [
    (None, "-"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4+", "4 ou plus"),
]

# Must be the same as static/js/forms/form.js:PHONE_REGEX
PHONE_REGEX = r"^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$"


def phoneNumberTest(phone):
    if re.match(PHONE_REGEX, str(phone)):
        raise ValidationError("Not a phone number")


class EventApplicationForm(forms.Form):
    school_level = forms.ChoiceField(
        label="Niveau d'études", choices=SCHOOL_LEVEL
    )

    # Info supplémentaires sur la participante
    nb_participations = forms.ChoiceField(
        label="La participante a-t-elle déjà participé à un stage Girls Can Code! ? Si oui, combien de fois ?",
        choices=NB_PARTICIPATIONS,
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
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "application_form"
        self.helper.form_method = "post"

        # Utility function to format a label tag ahead of input groups
        def labelize(s, required=False):
            label_class = 'class="requiredField"' if required else ""
            asterisk = (
                '<span class="asteriskField">*</span>' if required else ""
            )

            return HTML(f"<label {label_class}>{s}{asterisk}</label>")

        address_applicant = (
            labelize("Adresse", True),
            Field("street_applicant"),
            Field("complement_applicant"),
            Field("city_applicant"),
            Row(
                Column(Field("zip_code_applicant")),
                Column(Field("country_applicant")),
            ),
        )
        address_applicant_resp = (
            labelize("Adresse", True),
            Field("street_applicant_resp"),
            Field("complement_applicant_resp"),
            Field("city_applicant_resp"),
            Row(
                Column(Field("zip_code_applicant_resp")),
                Column(Field("country_applicant_resp")),
            ),
        )
        address_school = (
            labelize("Adresse", True),
            Field("street_school"),
            Field("complement_school"),
            Field("city_school"),
            Row(
                Column(Field("zip_code_school")),
                Column(Field("country_school")),
            ),
        )

        self.helper.layout = Layout(
            Div(
                HTML("<h2>Informations de la participante</h2>"),
                labelize("Identité", True),
                Row(
                    Column(Field("first_name")),
                    Column(Field("last_name")),
                ),
                Field("birthdate"),
                Field("email"),
                Field("phone"),
                *address_applicant,
                Field("is_women"),
                Field("legal_authorization"),
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
                HTML("<h2>Informations du responsable légal</h2>"),
                labelize("Identité", True),
                Row(
                    Column(Field("first_name_resp")),
                    Column(Field("last_name_resp")),
                ),
                Field("email_resp"),
                Field("phone_resp"),
                *address_applicant_resp,
                Div(
                    Row(
                        Column(
                            Button(
                                name="back",
                                value="Retour",
                                css_class="my-4 btn btn-light btn-block",
                            ),
                        ),
                        Column(
                            Button(
                                name="next",
                                value="Suivant",
                                css_class="my-4 btn btn-primary btn-block",
                            ),
                        ),
                    ),
                    css_class="mt-4 p-0",
                ),
                css_class="tab",
            ),
            Div(
                HTML("<h2>Informations sur l'établissement scolaire</h2>"),
                Field("name_school"),
                *address_school,
                Field("school_level"),
                Div(
                    Row(
                        Column(
                            Button(
                                name="back",
                                value="Retour",
                                css_class="my-4 btn btn-light btn-block",
                            ),
                        ),
                        Column(
                            Button(
                                name="next",
                                value="Suivant",
                                css_class="my-4 btn btn-primary btn-block",
                            ),
                        ),
                    ),
                    css_class="mt-4 p-0",
                ),
                css_class="tab",
            ),
            Div(
                Field("nb_participations"),
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

    def clean_school_info(self) -> Optional[dict]:
        if not self.is_valid():
            return None
        return {
            "school_level": self.cleaned_data["school_level"],
            "name": self.cleaned_data["name_school"],
            "street": self.cleaned_data["street_school"],
            "complement": self.cleaned_data["complement_school"],
            "city": self.cleaned_data["city_school"],
            "zip_code": self.cleaned_data["zip_code_school"],
            "country": self.cleaned_data["country_school"],
        }

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
