from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.http import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormMixin, UpdateView

from applications.forms import EventApplicationForm
from applications.models import Application, ApplicationStatus
from events.models import Event
from profiles.models import Profile
from users.models import User


class ApplicationsView(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = "applications/my_applications.html"
    form_class = EventApplicationForm

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        user_applications = Application.objects.filter(
            profile__user_id=self.request.user.id
        ).order_by("-created_at")

        ctx["applications"] = user_applications

        ctx["form"] = EventApplicationForm
        ctx["AppStatus"] = ApplicationStatus

        return ctx

    def get_form_kwargs(self):
        """
        Provide the rendered form with the profile choices of the current user
        """
        kw = super().get_form_kwargs()

        if self.request.user.is_authenticated:
            kw["profile_choices"] = Profile.get_choices_for_user(
                self.request.user
            )
        else:
            kw["profile_choices"] = [(None, "-")]

        return kw


class ApplicationCreateView(LoginRequiredMixin, View):
    http_method_names = ("post",)

    def post(self, request, *args, **kwargs):
        redirect_url = request.META.get("HTTP_REFERER", None)
        if not redirect_url:
            redirect_url = reverse("events:home")

        form = EventApplicationForm(request.POST)

        if not form.is_valid():
            messages.warning(
                request,
                str(form.errors),
            )
            return HttpResponseRedirect(redirect_url)
        else:
            form.save()
            messages.success(request, "Votre candidature a été enregistrée!")

            return HttpResponseRedirect(redirect_url)

    def http_method_not_allowed(self, request, *args, **kwargs):
        raise Http404()


class ApplicationStatusUpdateView(LoginRequiredMixin, View):
    http_method_names = ("post",)

    def post(self, request, *args, **kwargs):
        appid = self.kwargs.get("appid")
        transition = self.request.POST.get("transition")
        if not transition or not appid:
            return HttpResponseBadRequest("Bad request")

        application = Application.objects.get(id=appid)
        if not application:
            # Unknown application id
            return HttpResponseBadRequest("Bad request")

        if transition not in application.get_available_transitions_names(
            self.request.user
        ):
            # Illegal transition
            return HttpResponseBadRequest("Bad request")

        # The request is legitimate. Call the transition function of the
        # application, then save the application to the DB because the
        # transition does not do it.
        getattr(application, transition)()
        application.save()

        # We don't want to change the page
        current_page = request.META.get("HTTP_REFERER", None)
        if not current_page:
            return reverse("applications:my_applications")
        else:
            return HttpResponseRedirect(current_page)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Invalid method")


class ApplicationNotesUpdateView(PermissionRequiredMixin, UpdateView):
    permission = "user.can_view_application"
    http_method_names = ("post",)
    model = Application

    fields = ("notes",)

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", None)

    def get_object(self, *args, **kwargs):
        return Application.objects.get(id=self.request.POST["application-id"])
