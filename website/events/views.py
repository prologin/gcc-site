import datetime
from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView

from partners.models import Partner
from users.models import User

from .forms import EventSignupForm
from .models import events, signup


class UpdateStatusView(UpdateView):
    http_method_names = ("post",)
    modal = signup.Application
    success_url = reverse_lazy("events:my_applications")

    fields = ("status",)

    def get_object(self, *args, **kwargs):
        return signup.Application.objects.get(
            id=self.request.POST["application-id"]
        )


class HomePageView(ListView):
    model = events.Event
    template_name = "events/home.html"
    form_class = EventSignupForm
    paginate_by = 5

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

                address_resp = {
                    "street": request.POST["street_applicant_resp"],
                    "complement": request.POST["complement_applicant_resp"],
                    "city": request.POST["city_applicant_resp"],
                    "zip_code": request.POST["zip_code_applicant_resp"],
                    "country": request.POST["country_applicant_resp"],
                }

                school = {
                    "school_level": request.POST["school_level"],
                    "name": request.POST["name_school"],
                    "street": request.POST["street_school"],
                    "complement": request.POST["complement_school"],
                    "city": request.POST["city_school"],
                    "zip_code": request.POST["zip_code_school"],
                    "country": request.POST["country_school"],
                }

                form_answer = (
                    {
                        "tshirt": form.cleaned_data["tshirt"],
                        "allergies": form.cleaned_data["allergies"],
                        "diet": form.cleaned_data["diet"],
                        "learning": form.cleaned_data["learn"],
                        "programing": form.cleaned_data["programing"],
                        "studies": form.cleaned_data["studies"],
                        "association": form.cleaned_data["association"],
                    },
                )

                application = signup.Application.objects.create(
                    user=user,
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    dob=request.POST["dob"],
                    phone=request.POST["phone"],
                    address=address,
                    address_resp=address_resp,
                    school=school,
                    event=event,
                    form_answer=form_answer[0],
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
        p = Paginator(events.Event.objects.get_open_events(), self.paginate_by)

        page = ctx["page_obj"].number

        try:
            events_list = p.page(page)
        except PageNotAnInteger:
            events_list = p.page(1)
        except EmptyPage:
            events_list = p.page(p.num_pages)

        ctx["paginator"] = p
        ctx["open_events"] = events_list
        ctx["form"] = EventSignupForm

        ctx["partners_avant"] = Partner.objects.filter(status="Promoted")
        ctx["partners_financement"] = Partner.objects.filter(
            status="Financing"
        )
        ctx["partners_accueil"] = Partner.objects.filter(status="Welcoming")

        # Add a list of already applied events if authenticated
        if self.request.user.is_authenticated:
            ctx["already_applied"] = events.Event.objects.filter(
                id__in=signup.Application.objects.filter(
                    user=self.request.user.id
                ).values_list("event", flat=True)
            )

        ctx.update(signup.APPLICATION_STATUS)
        return ctx


class ReviewIndexView(PermissionRequiredMixin, TemplateView):
    permission_required = "users.can_view_applications"
    raise_exception = True
    template_name = "events/application/index.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["events"] = events.Event.objects.get_visible_events()
        return ctx


class ApplicationsReviewView(PermissionRequiredMixin, TemplateView):
    permission_required = "users.can_view_applications"
    template_name = "events/application/review.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["applications"] = signup.Application.objects.get_applicants(
            kwargs["event"]
        )
        ctx.update(signup.APPLICATION_STATUS)
        return ctx


class ApplicationsView(LoginRequiredMixin, TemplateView):
    template_name = "events/my_applications.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        user_applications = signup.Application.objects.filter(
            user=self.request.user.id
        ).order_by("-created_at")
        ctx["applications"] = user_applications

        ctx["form"] = EventSignupForm
        ctx.update(signup.APPLICATION_STATUS)
        return ctx


class EventListView(ListView):
    """
    This view might be given a "passed" keyword in the GET request.
    If so, it should
    """

    model = events.Event
    template_name = "events/event_list_page.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs_passed = qs.filter(end_date__date__lte=datetime.date.today())
        if "passed" in self.request.GET:
            # Only get events which ended today or before.
            # Show the most recent first
            return qs_passed.order_by("-end_date")
        else:
            # All event which are not passed
            # Show the soonest first
            return qs.difference(qs_passed).order_by("start_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EventSignupForm
        return context
