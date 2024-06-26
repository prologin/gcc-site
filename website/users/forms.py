from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Field, Layout, Row, Submit
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    BaseUserCreationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.core.validators import validate_email
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class PersonalInfoForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=80, required=True)
    last_name = forms.CharField(
        label="Nom",
        max_length=80,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "personal_info_form"
        self.helper.form_method = "post"
        self.helper.form_action = reverse_lazy("users:update_user_info")

        name_layout = Row(
            Column(
                Field(
                    "last_name",
                    placeholder=self.fields["last_name"].label,
                )
            ),
            Column(
                Field(
                    "first_name",
                    placeholder=self.fields["first_name"].label,
                )
            ),
        )

        submit = Div(
            Submit(
                "submit-personal_info",
                "Sauvegarder",
                css_class="btn btn-primary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            name_layout,
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
        self.helper.form_action = reverse_lazy("users:update_user_email")

        submit = Div(
            Submit(
                "submit-email",
                "Sauvegarder",
                css_class="btn btn-primary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            Field("email", placeholder=self.fields["email"].label),
            submit,
        )


class UserPasswordUpdateForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "password_update_form"
        self.helper.form_method = "post"
        self.helper.form_action = reverse_lazy("users:update_password")

        submit = Div(
            Submit(
                "submit-password",
                "Sauvegarder",
                css_class="btn btn-primary btn-block",
            ),
            css_class="mt-4 p-0 col-12 col-md-4 offset-md-8 col",
        )

        self.helper.layout = Layout(
            Field("old_password", placeholder=""),
            Field("new_password1", placeholder=""),
            Field("new_password2", placeholder=""),
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
                css_class="btn btn-primary btn-block",
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
        self.helper.form_method = "post"  # Corrected typo here
        self.helper.form_action = reverse_lazy("users:delete_user")
        self.helper.layout = Layout(
            Submit(
                name="submit-delete-user",
                value="Supprimer",
                css_class="btn btn-primary btn-block red-button",
            )
        )


class AuthLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "notifs_update_form"
        self.helper.form_method = "post"
        self.error_messages = {
            "invalid_login": _(
                "Saisissez un Adresse email et un mot de passe valides. Remarquez que chacun de ces champs est sensible à la casse (différenciation des majuscules/minuscules)."
            ),
            "inactive": _(
                "Votre compte n'est pas encore activé. Veuillez vérifier vos e-mails pour trouver le lien d'activation."
            ),
        }

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

    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit(
                None,
                value=_("Créer mon compte"),
                css_class="btn btn-primary btn-block",
            )
        )


class GCCPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("submit", "Réinitialiser mon mot de passe")
        )


class GCCPasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("submit", "Réinitialiser mon mot de passe")
        )
