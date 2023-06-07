from crispy_forms.bootstrap import InlineCheckboxes
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
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


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
    country = forms.CharField(
        label="Pays",
        max_length=80,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "personal_info_form"
        self.helper.form_method = "post"

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

        submit = Div(
            Submit(
                "submit-personal_info",
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

        submit = Div(
            Submit(
                "submit-email",
                "Sauvegarder",
                css_class="btn primary-button btn-secondary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            Field("email", placeholder=self.fields["email"].label),
            submit,
        )


class PasswordUpdateForm(forms.Form):
    current_pwd = forms.CharField(
        label="Mot de passe actuel", widget=forms.PasswordInput, required=True
    )
    new_pwd = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput,
        required=True,
        validators=[validate_password],
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

        submit = Div(
            Submit(
                "submit-password",
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

        submit = Div(
            Submit(
                "submit-notifications",
                "Sauvegarder",
                css_class="btn primary-button btn-secondary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            InlineCheckboxes("accept_notifs", css_class="region_checkboxes"),
            submit,
        )


class DeleteUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "delete_user_form"
        self.form_method = "post"

        self.helper.layout = Layout(
            Submit(
                name="submit-delete-user",
                value="Supprimer",
                css_class="btn primary-button red-button btn-secondary btn-block"
            )
        )


class AuthLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "notifs_update_form"
        self.helper.form_method = "post"

        submit = Div(
            Submit(
                name="submit-notifications",
                value="Se connecter",
                css_class="btn btn-block",
            ),
            css_class="mt-4 p-0",
        )

        self.helper.layout = Layout(
            Field("username"), Field("password"), submit
        )


class AuthRegisterForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")
        field_classes = {"email": forms.EmailField}

    authorization = forms.BooleanField(
        label=_(
            "J'ai plus de 15 ans OU l'autorisation de mon responsable légal pour m'inscrire"
        ),
        error_messages={
            "required": _(
                "Tu ne peux pas t'inscrire sur ce site sans l'autorisation de ton responsable légal si tu as 15 ans ou moins"
            ),
        },
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "register_form"
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            # First tab
            Div(
                Field("first_name"),
                Field("last_name"),
                Button(
                    name="next",
                    value="Suivant",
                    css_class="btn btn-secondary btn-block",
                ),
                css_class="tab",
            ),
            # Second tab
            Div(
                Field("email"),
                Field("password1"),
                Field("password2"),
                Field("authorization"),
                Submit(
                    name="submit-registration",
                    value="Créer mon compte",
                    css_class="btn btn-block",
                ),
                Button(
                    name="back",
                    value="Précédent",
                    css_class="mt-4 btn btn-block btn-secondary",
                ),
                css_class="tab",
            ),
        )
