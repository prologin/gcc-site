import csv
from typing import Any

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import (
    default_token_generator as account_activation_token,
)
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
    RedirectURLMixin,
)
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView, DeleteView, TemplateView
from django.views.generic.edit import UpdateView

from applications.models import Application
from profiles.models import Profile

from .forms import (
    AuthLoginForm,
    AuthRegisterForm,
    DeleteUserForm,
    EmailForm,
    GCCPasswordResetConfirmForm,
    GCCPasswordResetForm,
    NotificationsUpdateForm,
    PersonalInfoForm,
    UserPasswordUpdateForm,
)
from .models import User

# Extra message tags
TAG_PERSONAL_INFO = "personal_info"
TAG_EMAIL = "email"
TAG_PWD = "pwd"


class UserEditView(LoginRequiredMixin, UpdateView):
    http_method_names = ("post",)
    model = User
    fields = (
        "first_name",
        "last_name",
    )

    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("users:account_information") + "#personal-info"


class UserEmailEditView(LoginRequiredMixin, UpdateView):
    http_method_names = ("post",)
    model = User
    fields = ("email",)

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.id)

    def form_valid(self, form):
        user_data = {
            "pk": self.request.user.pk,
            "email": form.cleaned_data["email"],
        }
        token = signing.dumps(user_data)
        self.send_activation_email(
            self.request.user, form.cleaned_data["email"], token
        )
        messages.info(
            self.request,
            _(
                "Un mail de vérification a été envoyé à l'adresse renseignée. Merci de cliquer sur le lien donné dans le mail pour compléter la mise à jour de votre adresse email."
            ),
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(
            self.request, _("L'email est invalide"), extra_tags=TAG_EMAIL
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("users:account_information") + "#personal-info"

    def send_activation_email(self, user, email, token):
        subject = _("Activez votre nouvelle adresse email!")
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        activation_link = "{}{}".format(
            get_current_site(self.request),
            reverse("users:verify_email", args=[uid, token]),
        )

        message = render_to_string(
            template_name="users/mails/email_activation_link.txt",
            context={
                "firstname": user.first_name,
                "lastname": user.last_name,
                "link": activation_link,
            },
        )
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])


class ActivateEmailView(View):
    def invalid_link(self):
        messages.error(
            self.request, _("Le lien d'activation est invalide ou a expiré.")
        )
        return redirect(settings.LOGIN_URL)

    def activate_email(self):
        self.user.email = self.user_data.get("email")
        self.user.save()

    def get_success_url(self):
        messages.success(
            self.request,
            _("Votre mail a été modifié !"),
        )
        return reverse("events:home")

    def get(self, request, uidb64, token):
        try:
            self.user_data = signing.loads(token)
            uid = self.user_data.get("pk")
            self.user = User.objects.get(pk=uid)
        except (signing.BadSignature, User.DoesNotExist):
            return self.invalid_link()

        if self.user and "email" in self.user_data:
            self.activate_email()
            return redirect(self.get_success_url())
        else:
            return self.invalid_link()


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/password_reset/password_reset.html"
    form_class = UserPasswordUpdateForm
    success_url = reverse_lazy("users:account_information")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page_title"] = "Changement de mot de passe"
        return ctx


class ExportUsersCSVView(LoginRequiredMixin, View):
    model = User

    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(["First Name", "Last Name", "Email"])

        user = User.objects.get(id=self.request.user.id)
        profiles = Profile.objects.filter(user_id=self.request.user.id)
        applications = Application.objects.filter(
            profile__user_id=self.request.user.id
        ).order_by("-created_at")

        writer.writerow([user.first_name, user.last_name, user.email])

        writer.writerow(["Profil"])
        writer.writerow(
            [
                "first_name",
                "last_name",
                "birth_date",
                "email",
                "phone",
                "street_app",
                "complement_app",
                "city_app",
                "zipcode_app",
                "country_app",
                "first_name_resp",
                "last_name_resp",
                "email_resp",
                "phone_resp",
                "street_resp",
                "complement_resp",
                "city_resp",
                "zipcode_resp",
                "country_resp",
                "school_name",
                "street_school",
                "complement_school",
                "city_school",
                "zipcode_school",
                "country_school",
            ]
        )

        for profile in profiles:
            # Add application data to the CSV row
            writer.writerow(
                [
                    profile.first_name,
                    profile.last_name,
                    profile.birth_date,
                    profile.email,
                    profile.phone,
                    profile.street_app,
                    profile.complement_app,
                    profile.city_app,
                    profile.zipcode_app,
                    profile.country_app,
                    profile.first_name_resp,
                    profile.last_name_resp,
                    profile.email_resp,
                    profile.phone_resp,
                    profile.street_resp,
                    profile.complement_resp,
                    profile.city_resp,
                    profile.zipcode_resp,
                    profile.country_resp,
                    profile.school_name,
                    profile.street_school,
                    profile.complement_school,
                    profile.city_school,
                    profile.zipcode_school,
                    profile.country_school,
                ]
            )

        writer.writerow(["application"])
        writer.writerow(
            [
                "profile",
                "school",
                "form_answer",
                "created at",
            ]
        )

        for application in applications:
            # Add application data to the CSV row
            writer.writerow(
                [
                    application.profile,
                    application.form_answer,
                    application.created_at,
                ]
            )

        return response

    def get_object(self, *args, **kwargs):
        return self.request.user


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    http_method_names = ("post",)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, _("L'utilisateur a été supprimé"))
        return reverse("events:home")

    def delete(self, request, *args, **kwargs):
        # You can add additional checks here if needed before deletion
        return super().delete(request, *args, **kwargs)


class AccountInformationsView(LoginRequiredMixin, TemplateView):
    template_name = "users/AccountInformationsView.html"

    def get_context_data(self, **kwargs: Any):
        # Get the request user to prefill the forms
        user = self.request.user

        user_data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }

        return {
            "personal_info_form": PersonalInfoForm(user_data),
            "email_form": EmailForm(user_data),
            "notifs_update_form": NotificationsUpdateForm(),
            "delete_user_form": DeleteUserForm(),
        }


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"
    form_class = AuthLoginForm
    redirect_authenticated_user = True


class RegisterView(RedirectURLMixin, CreateView):
    template_name = "users/register.html"
    form_class = AuthRegisterForm
    next_page = settings.LOGIN_REDIRECT_URL

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        """
        Like for the Login View, prevent the access of logged users to this page
        """
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Save the user instance without committing it to the database yet
        user = form.save(commit=False)
        user.is_active = False  # Set the user's active status to False until they activate their account
        user.save()

        # Send the activation email to the user
        self.send_activation_email(user, form.cleaned_data["email"])

        messages.info(
            self.request,
            _(
                "Activez votre compte en cliquant sur le lien envoyé à votre adresse mail"
            ),
        )
        return HttpResponseRedirect(self.get_success_url())

    def send_activation_email(self, user, email):
        subject = _("Activez votre compte Girls Can Code!")
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)

        activation_link = "{}{}".format(
            get_current_site(self.request),
            reverse("users:activate", args=[uid, token]),
        )

        email_from = settings.DEFAULT_FROM_EMAIL
        message = render_to_string(
            template_name="users/mails/account_activation_link.txt",
            context={
                "firstname": user.first_name,
                "lastname": user.last_name,
                "link": activation_link,
            },
        )
        send_mail(subject, message, email_from, [email])


class ActivateAccountView(View):
    def invalid_link(self):
        messages.error(
            self.request, _("Le lien d'activation est invalide ou a expiré.")
        )
        return redirect(settings.LOGIN_URL)

    def activate_account(self):
        self.user.is_active = True
        self.user.save()

    def get_success_url(self):
        messages.success(
            self.request,
            _("Votre compte a été activé ! Vous pouvez vous connecter."),
        )
        return settings.LOGIN_URL

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            self.user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return self.invalid_link()

        if self.user and account_activation_token.check_token(
            self.user, token
        ):
            self.activate_account()
            return redirect(self.get_success_url())
        else:
            return self.invalid_link()


class GCCPasswordResetView(PasswordResetView):
    template_name = "users/password_reset/password_reset.html"
    form_class = GCCPasswordResetForm
    email_template_name = "users/password_reset/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")

    def get_context_data(self):
        ctx = super().get_context_data()
        ctx["page_title"] = "Réinitialiser son mot de passe"
        return ctx


class GCCPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset/password_reset_done.html"


class GCCPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset/password_reset_confirm.html"
    form_class = GCCPasswordResetConfirmForm
    success_url = reverse_lazy("users:password_reset_complete")


class GCCPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset/password_reset_complete.html"
    success_url = reverse_lazy("users:login")
