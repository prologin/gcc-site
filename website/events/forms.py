import re

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
    (
        None,
        "------ Selectionner ton niveau d'étude actuel ------",
    ),  # Start choice
    ("6ème", "6ème"),
    ("5ème", "5ème"),
    ("4ème", "4ème"),
    ("3ème", "3ème"),
    ("Seconde", "Seconde"),
    ("Première", "Première"),
    ("Terminale", "Terminale"),
]

TSHIRT = [
    (None, "------ Selectionner une taille de t-shirt ------"),
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("XXL", "XXL"),
]

NB_PARTICIPATIONS = [
    (None, "------ Selectionner un nombre de participations ------"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4 ou plus", "4 ou plus"),
]

# Must be the same as static/js/forms/form.js:PHONE_REGEX
PHONE_REGEX = "^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$"


def phoneNumberTest(phone):
    if re.match(PHONE_REGEX, str(phone)):
        raise ValidationError("Not a phone number")


class EventSignupForm(forms.Form):
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
            attrs={"placeholder": "Complément d'adresse", "blank": True}
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
                "placeholder": "Complément d'adresse du responsable légal",
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
        label="Y a-t-il des études en informatique qui intéresseraient la participante ? Si oui, pourrais-t'elle préciser lesquelles ?",
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
