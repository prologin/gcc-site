from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from users.models import User

from .forms import EventSignupForm
from .models import events, signup


class HomePageView(TemplateView):
    template_name = "events/home.html"
    form_class = EventSignupForm

    def post(self, request, *args, **kwargs):
        if "submit-application" in request.POST:
            form = EventSignupForm(request.POST)

            if not form.is_valid():
                messages.warning(
                    request,
                    str(form.errors),
                )
                return HttpResponseRedirect(reverse("events:home"))
            else:
                event = events.Event.objects.get(id=request.POST["event-id"])
                user = User.objects.get(id=request.user.id)

                address = {
                    "street": request.POST["street_applicant"],
                    "complement": request.POST["complement_applicant"],
                    "city": request.POST["city_applicant"],
                    "zip_code": request.POST["zip_code_applicant"],
                    "country": request.POST["country_applicant"],
                }

                form_answer = (
                    {
                        "tshirt": request.POST["tshirt"],
                        "allergies": request.POST["allergies"],
                        "diet": request.POST["diet"],
                        "learning": request.POST["learn"],
                        "programing": request.POST["programing"],
                        "studies": request.POST["studies"],
                        "association": request.POST["association"],
                    },
                )

                school = {
                    "school_level": request.POST["school_level"],
                    "name": request.POST["name_school"],
                    "street": request.POST["street_school"],
                    "complement": request.POST["complement_school"],
                    "city": request.POST["city_school"],
                    "zip_code": request.POST["zip_code_school"],
                    "country": request.POST["country_school"],
                }

                application = signup.Application.objects.create(
                    user=user,
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    dob=request.POST["dob"],
                    phone=request.POST["phone"],
                    address=address,
                    school=school,
                    event=event,
                    form_answer=form_answer,
                )

                messages.success(
                    request, "Votre candidature a été enregistré!"
                )

                return HttpResponseRedirect(reverse("events:home"))
        elif "submit-newsletter" in request.POST:
            # TODO : DO SOMETHING HERE ?

            return HttpResponseRedirect(reverse("events:home"))

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["open_events"] = events.Event.objects.get_open_events()
        ctx["form"] = EventSignupForm
        return ctx


class ReviewIndexView(TemplateView):
    template_name = "events/application/index.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["open_events"] = events.Event.objects.get_open_events()
        ctx["events"] = events.Event.objects.get_visible_events()
        return ctx


class ApplicationsReviewView(TemplateView):
    template_name = "events/application/review.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        print(kwargs)
        ctx["applications"] = signup.Application.objects.get_applicants(
            kwargs["event"]
        )
        return ctx


class ApplicationsView(LoginRequiredMixin, TemplateView):
    template_name = "events/mes-candidatures.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["application_documents"] = signup.Application.objects.filter(
            user=self.request.user.id
        ).order_by("-created_at")
        return ctx
