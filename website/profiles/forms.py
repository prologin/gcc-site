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

from profiles import models

# Must be the same as static/js/forms/form.js:PHONE_REGEX
PHONE_REGEX = r"^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$"


def phoneNumberTest(phone):
    if re.match(PHONE_REGEX, str(phone)):
        raise ValidationError("Not a phone number")


class ProfileCreationForm(forms.ModelForm):
    # Info sur la participante
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Prénom"}),
        max_length=255,
    )

    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Nom de famille"}),
        max_length=255,
    )

    dob = forms.DateField(
        label="Date de naissance",
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
    )

    phone = forms.DecimalField(
        label="Numéro de téléphone",
        validators=[phoneNumberTest],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Numéro de téléphone",
                "type": "tel",
            }
        ),
    )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
        max_length=320,
        required=True,
        validators=[validate_email],
    )

    is_women = forms.BooleanField(
        label=_("La participante se considère comme une femme."),
        error_messages={
            "required": _(
                "Tu ne peux pas t'inscrire aux stages Girls Can Code! si tu ne te considères pas comme femme."
            ),
        },
    )

    legal_authorization = forms.BooleanField(
        label=_(
            "La participante a plus de 15 ans OU l'autorisation de son responsable légal pour candidater à ce stage."
        ),
        error_messages={
            "required": _(
                "La participante ne peux pas s'inscrire à ce stage sans l'autorisation de son responsable légal ou si elle a 15 ans ou moins."
            ),
        },
    )

    # Adresse de la participante

    street_applicant = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Nom et numéro de voie"}),
        max_length=250,
    )

    complement_applicant = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Complément d'adresse (si nécessaire)",
                "blank": True,
            }
        ),
        max_length=200,
        required=False,
    )

    city_applicant = forms.CharField(
        label="",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ville"}),
    )

    zip_code_applicant = forms.IntegerField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Code postal", "type": "number"}
        ),
    )

    country_applicant = forms.CharField(
        label="",
        max_length=30,
        initial="France",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Pays"}),
    )

    # Responsable légal de la participante
    first_name_resp = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Prénom"}),
        max_length=255,
    )

    last_name_resp = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Nom de famille"}),
        max_length=255,
    )

    email_resp = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
        max_length=320,
        required=True,
        validators=[validate_email],
    )

    phone_resp = forms.DecimalField(
        label="Numéro de téléphone",
        validators=[phoneNumberTest],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Numéro de téléphone",
                "type": "tel",
            }
        ),
    )

    street_applicant_resp = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Nom et numéro de voie du responsable légal"}
        ),
        max_length=250,
    )

    complement_applicant_resp = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Complément d'adresse du responsable légal (si nécessaire)",
                "blank": True,
            }
        ),
        max_length=200,
        required=False,
    )

    city_applicant_resp = forms.CharField(
        label="",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Ville du responsable légal"}
        ),
    )

    zip_code_applicant_resp = forms.IntegerField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Code postal du responsable légal",
                "type": "number",
            }
        ),
    )

    country_applicant_resp = forms.CharField(
        label="",
        max_length=30,
        initial="France",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Pays"}),
    )

    # Etablissement scolaire

    name_school = forms.CharField(
        label="Nom",
        widget=forms.TextInput(
            attrs={"placeholder": "Nom de l'établissement scolaire"}
        ),
        max_length=255,
    )

    street_school = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Nom et numéro de voie"}),
        max_length=250,
    )

    complement_school = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Complément d'adresse"}),
        max_length=200,
        required=False,
    )

    city_school = forms.CharField(
        label="",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ville"}),
    )

    zip_code_school = forms.IntegerField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Code postal", "type": "number"}
        ),
    )

    country_school = forms.CharField(
        label="",
        max_length=30,
        initial="France",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Pays"}),
    )

    class Meta:
        model = models.Profile
        fields = (
            "last_name",
            "first_name",
            "phone",
            "dob",
            "address",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "profile_creation_form"
        self.helper.form_method = "post"
        self.helper.form_action = reverse_lazy("profiles:profiles_create")

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
                Field("dob"),
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
                            Submit(
                                name="submit-application",
                                value="Créer mon profil",
                                css_class="my-4 btn btn-primary btn-block",
                            )
                        ),
                    ),
                    css_class="mt-4 p-0",
                ),
                css_class="tab",
            ),
        )

    def clean_address(self) -> Optional[dict]:
        if not self.is_valid():
            return None
        return {
            "street": self.cleaned_data["street_applicant"],
            "complement": self.cleaned_data["complement_applicant"],
            "city": self.cleaned_data["city_applicant"],
            "zip_code": self.cleaned_data["zip_code_applicant"],
            "country": self.cleaned_data["country_applicant"],
        }

    def clean_address_resp(self) -> Optional[dict]:
        if not self.is_valid():
            return None
        return {
            "street": self.cleaned_data["street_applicant_resp"],
            "complement": self.cleaned_data["complement_applicant_resp"],
            "city": self.cleaned_data["city_applicant_resp"],
            "zip_code": self.cleaned_data["zip_code_applicant_resp"],
            "country": self.cleaned_data["country_applicant_resp"],
        }

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
