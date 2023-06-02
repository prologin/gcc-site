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
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class EventSignupForm(forms.Form):
    first_name = forms.CharField(
        label="Prénom",
        max_length=256,
        required=True
    )

    last_name = forms.CharField(
        label="Nom de famille",
        max_length=256,
        required=True
    )

    dob = forms.DateField(
        label="Date de naissance",
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        required=True
    )
    
    address = forms.CharField(
        label=("Addresse: Ville, zipcode, pays"),
        required=True
    )

    email = forms.EmailField(
        label="E-mail",
        max_length=320,
        required=True,
        validators=[validate_email],
    )

    phone = forms.RegexField(regex="^(?:(?:\\+|00)33|0)\\s*[1-9](?:[\\s.-]*\\d{2}){4}$")

    authorization = forms.BooleanField(
        label=_(
            "Je certifie que je m'identifie comme une femme"
        ),
        error_messages={
            "required": _(
                "Nos stages Girls Can Code! sont réservés aux femmes"
            ),
        },
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "application_form"
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Div(
                Button(
                    name="self_inscription",
                    value="M'inscrire",
                    css_class = "next-click btn primary-button",
                ),
                Button(
                    name="child_inscription",
                    value="Inscrire ma fille",
                    css_class = "next-click btn primary-button",
                ),
                css_class = "tab active"
            ),
            Div(
                Field("first_name"),
                Field("last_name"),
                Field("dob"),
                Field("email"),
                Field("address"),
                Field("phone"),
                Field("authorization"),
                Div(
                    Button(
                        name="back",
                        value="Retour",
                        css_class="back-click btn primary-button",
                    ),
                    Button(
                        name="next",
                        value="Suivant",
                        css_class="next-click btn primary-button",
                    ),
                    css_class="mt-4 p-0",
                ),
                css_class = "tab"
            )
        )
