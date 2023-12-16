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


class ProfileCreationForm(forms.ModelForm):

    email = forms.EmailField(
        label=_("Adresse email"),
        required=True
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

    zip_code_applicant = forms.CharField(
        label="",
        max_length=16,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Code postal",
            }
        ),
    )

    country_applicant = forms.CharField(
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
            "birth_date",
            "address",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "profile_creation_form"
        self.helper.form_method = "post"
        self.helper.form_action = reverse_lazy("users:profiles_create")

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
            Field("zip_code_applicant"),
            Row(
                Column(Field("city_applicant")),
                Column(Field("country_applicant")),
            ),
        )

        name_layout = Row(
            Field(
                "email",
                placeholder=self.fields["email"].label
            ),
            Row(
                Column(Field(
                    "last_name",
                    placeholder=self.fields["last_name"].label
                )),
                Column(Field(
                    "first_name",
                    placeholder=self.fields["first_name"].label,
                ))
            ),
            Row(
                Column(Field(
                "phone",
                placeholder=self.fields["phone"].label,
                )),
                Column(Field(
                    "birth_date",
                placeholder=self.fields["birth_date"].label
                )),
            ),
            *address_applicant,
            Field(
                    "is_women",
                placeholder=self.fields["birth_date"].label
            ),
        )

        submit = Div(
            Submit(
                "submit-create_profile",
                "Sauvegarder",
                css_class="btn btn-primary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            name_layout,
            submit,
        )