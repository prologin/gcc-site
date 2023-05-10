from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Div, Field, Layout, Row, Submit
from django import forms
from django.core.validators import validate_email
from django_countries.fields import CountryField


class PersonalInfoForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=80, required=True)
    last_name = forms.CharField(
        label="Nom",
        max_length=80,
        required=True,
    )
    street = forms.CharField(
        label="Nom et numéro de voie",
        max_length=256,
        required=False,
    )
    zip_code = forms.CharField(
        label="Code postal",
        max_length=10,
        required=False,
    )
    city = forms.CharField(
        label="Ville",
        max_length=80,
        required=False,
    )
    # According to https://pypi.org/project/django-countries/#custom-forms
    country = CountryField().formfield(required=False)

    birth_date = forms.DateField(
        label="Date de naissance",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "personal_info_form"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        name_layout = Row(
            Column(
                Field("last_name", placeholder=self.fields["last_name"].label)
            ),
            Column(
                Field(
                    "first_name", placeholder=self.fields["first_name"].label
                )
            ),
        )
        address_layout = Div(
            HTML('<div style="margin-bottom: 8px">Adresse</div>'),
            Row(Field("street", placeholder=self.fields["street"].label)),
            Row(
                Column(
                    Field(
                        "zip_code", placeholder=self.fields["zip_code"].label
                    )
                ),
                Column(Field("city", placeholder=self.fields["city"].label)),
            ),
            Row(Field("country", placeholder=self.fields["country"].label)),
        )
        birth_date_layout = Div(Field("birth_date"))

        submit = Div(
            Submit(
                "submit",
                "Sauvegarder",
                css_class="btn primary-button btn-secondary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        # Disable the label of address fields
        self.fields["street"].label = False
        self.fields["zip_code"].label = False
        self.fields["city"].label = False
        self.fields["country"].label = False

        self.helper.layout = Layout(
            name_layout,
            birth_date_layout,
            address_layout,
            submit,
        )


class EmailForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
        max_length=320,
        required=True,
        validators=[validate_email],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "email_form"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        submit = Div(
            Submit(
                "submit",
                "Sauvegarder",
                css_class="btn primary-button btn-secondary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            Field("email", placeholder="Nouvelle adresse e-mail"),
            submit,
        )


class PasswordUpdateForm(forms.Form):
    current_pwd = forms.CharField(
        label="Mot de passe actuel", widget=forms.PasswordInput, required=True
    )
    new_pwd = forms.CharField(
        label="Nouveau mot de passe", widget=forms.PasswordInput, required=True
    )
    new_pwd_ack = forms.CharField(
        label="Confirmer le nouveau mot de passe",
        widget=forms.PasswordInput,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "password_update_form"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        submit = Div(
            Submit(
                "submit",
                "Sauvegarder",
                css_class="btn primary-button btn-secondary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            Field("current_pwd", placeholder=""),
            Field("new_pwd", placeholder=""),
            Field("new_pwd_ack", placeholder=""),
            submit,
        )


class NotificationsUpdateForm(forms.Form):
    accept_notifs = forms.MultipleChoiceField(
        label="Je souhaite être notifiée par e-mail des prochains stages ayant lieu dans les régions suivantes",
        choices=(
            ("1", "Nord-Ouest"),
            ("2", "Est"),
            ("3", "Ile-de-France"),
            ("4", "Ouest"),
            ("5", "Sud"),
            ("6", "DROM-COM"),
        ),
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "notifs_update_form"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        submit = Div(
            Submit(
                "submit",
                "Sauvegarder",
                css_class="btn primary-button btn-secondary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            InlineCheckboxes("accept_notifs", css_class="region_checkboxes"),
            submit,
        )
