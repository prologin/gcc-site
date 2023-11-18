from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.views.generic.edit import UpdateView

from applications.forms import EventApplicationForm
from applications.models import APPLICATION_STATUS, Application
from events.models import Event
from users.models import User


class ApplicationsView(LoginRequiredMixin, TemplateView):
    template_name = "applications/my_applications.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        user_applications = Application.objects.filter(
            user=self.request.user.id
        ).order_by("-created_at")

        ctx["applications"] = user_applications

        ctx["form"] = EventApplicationForm
        ctx.update(APPLICATION_STATUS)

        return ctx


class ApplicationCreateView(LoginRequiredMixin, View):
    http_method_names = ("post",)

    def post(self, request, *args, **kwargs):
        redirect_url = request.META.get("HTTP_REFERER", None)
        if not redirect_url:
            redirect_url = reverse("events:home")

        if "submit-application" in request.POST:
            form = EventApplicationForm(request.POST)

            if not form.is_valid():
                messages.warning(
                    request,
                    str(form.errors),
                )
                return HttpResponseRedirect(redirect_url)
            else:
                event = Event.objects.get(id=request.POST["event-id"])
                user = User.objects.get(id=request.user.id)

                address = form.clean_address()

                address_resp = form.clean_address_resp()

                school = form.clean_school_info()

                form_answer = form.clean_form_answers()

                application = Application.objects.create(
                    user=user,
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    dob=form.cleaned_data["birthdate"],
                    email=form.cleaned_data["email"],
                    phone=form.cleaned_data["phone"],
                    address=address,
                    first_name_resp=form.cleaned_data["first_name_resp"],
                    last_name_resp=form.cleaned_data["last_name_resp"],
                    email_resp=form.cleaned_data["email_resp"],
                    phone_resp=form.cleaned_data["phone"],
                    address_resp=address_resp,
                    school=school,
                    event=event,
                    form_answer=form_answer[0],
                    nb_participations=form.cleaned_data["nb_participations"],
                )

                messages.success(
                    request, "Votre candidature a été enregistrée!"
                )

                return HttpResponseRedirect(redirect_url)

    def http_method_not_allowed(self, request, *args, **kwargs):
        raise Http404()


class ApplicationStatusUpdateView(LoginRequiredMixin, UpdateView):
    http_method_names = ("post",)
    model = Application
    fields = ("status",)

    def get_object(self, *args, **kwargs):
        return Application.objects.get(id=self.request.POST["application-id"])

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", None)


class ApplicationNotesUpdateView(PermissionRequiredMixin, UpdateView):
    permission = "user.can_view_application"
    http_method_names = ("post",)
    model = Application

    fields = ("notes",)

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", None)

    def get_object(self, *args, **kwargs):
        return Application.objects.get(id=self.request.POST["application-id"])
