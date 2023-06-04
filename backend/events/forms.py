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
from django.core.validators import RegexValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _


class EventSignupForm(forms.Form):
    # Info sur la participante
    first_name = forms.CharField(
        label="Prénom de la participante:",
        max_length=256,
        required=True
    )

    last_name = forms.CharField(
        label="Nom de famille de la participante: ",
        max_length=256,
        required=True
    )

    dob = forms.DateField(
        label="Date de naissance de la participante: ",
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        required=True
    )

    city = forms.CharField(label="Ville", max_length=50)
    zip_code = forms.IntegerField(label="Code postal")
    country = forms.CharField(label="Pays", max_length=30, initial="France")

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

    # Responsable légal

    phone = forms.DecimalField(
        label="Numéro de téléphone du responsable légal",
        validators=[RegexValidator(
            regex="^(?:(?:\\+|00)33|0)\\s*[1-9](?:[\\s.-]*\\d{2}){4}$",
            message="Not a phone number",
            code="invalid_phone")],
        required=True,
    )

    # Info supplémentaires participantes

    diet = forms.CharField(
        label="As-tu un régime alimentaire particulier ?",
        max_length=256,
        required=True
    )

    allergies = forms.CharField(
        label="As-tu des allergies ?",
        max_length=256,
        required=True
    )

    tshirt = forms.CharField(
        label="Quelle est ta taille de t-shirt ?",
        help_text="Un t-shirt sera donné aux participantes pendant le stage",
        max_length=256,
        required=True
    )

    learn = forms.CharField(
        label="Y-a-t’il quelque chose en particulier que tu espères apprendre pendant le stage ? (2 à 3 phrases)",
        max_length=256,
        required=True
    )

    programing = forms.CharField(
        label="As-tu déjà programmé, si oui, quand as-tu codé pour la première fois et quels outils ou langages de programmation as-tu essayés ?",
        max_length=256,
        required=True
    )

    studies = forms.CharField(
        label="Y a-t-il des études en informatique qui t'intéresseraient ? Si oui, pourrais-tu préciser lesquelles ?",
        max_length=256,
        required=True
    )

    association = forms.CharField(
        label="Comment as-tu connu l'association et les stages ? Essaye d'être précise, cela nous aide beaucoup !",
        max_length=256,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "application_form"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Div(
                Field("first_name"),
                Field("last_name"),
                Field("dob"),
                Field("city"),
                Field("zip_code"),
                Field("country"),
                Field("phone"),
                Field("authorization"),
                Div(
                    Button(
                        name="next",
                        value="Suivant",
                        css_class="btn primary-button"
                    ),
                    css_class="mt-4 p-0"
                ),
                css_class="tab active"
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
                    Button(
                        name="back",
                        value="Retour",
                        css_class="btn primary-button"
                    ),
                    Submit(
                        name="submit-application",
                        value="Candidater pour ce stage",
                        css_class="mt-4 btn btn-block",
                    ),
                    css_class="mt-4 p-0"
                ),
                css_class="tab"
            )
        )
