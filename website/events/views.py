import datetime

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormMixin

from applications.forms import EventApplicationForm
from applications.models import Application, ApplicationStatus
from events.models import Event
from partners.models import Partner
from profiles.models import Profile


class HomePageView(ListView):
    model = Event
    template_name = "events/home.html"
    form_class = EventApplicationForm

    def post(self, request, *args, **kwargs):
        if "submit-newsletter" in request.POST:
            # TODO : DO SOMETHING HERE ?

            return HttpResponseRedirect(reverse("events:home"))

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx["open_events"] = Event.objects.get_open_events(5)
        form = EventApplicationForm(profile_choices=[])
        ctx["form"] = form

        ctx["partners_avant"] = Partner.objects.filter(status="Promoted")
        ctx["partners_financement"] = Partner.objects.filter(
            status="Financing"
        )
        ctx["partners_accueil"] = Partner.objects.filter(status="Welcoming")

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


class ReviewIndexView(PermissionRequiredMixin, TemplateView):
    permission_required = "users.can_view_applications"
    raise_exception = True
    template_name = "events/application/index.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["years"] = Event.objects.years()
        if self.request.GET:
            ctx["events"] = Event.objects.filter(year=self.request.GET["year"])
        else:
            ctx["events"] = Event.objects.get_visible_events()
        ctx["AppStatus"] = ApplicationStatus
        return ctx


class ApplicationsReviewView(PermissionRequiredMixin, TemplateView):
    permission_required = "users.can_view_applications"
    template_name = "events/application/review.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["applications"] = Application.objects.get_applicants(
            kwargs["event"]
        )
        ctx["AppStatus"] = ApplicationStatus
        return ctx


class EventListViewBase(FormMixin, ListView):
    model = Event
    template_name = "events/event_list_page.html"
    # Show 5 elements per page
    paginate_by = 10

    form_class = EventApplicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["passed"] = False
        return context

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


class EventListView(EventListViewBase):
    def get_queryset(self):
        qs = super().get_queryset()
        qs_passed = qs.filter(end_date__date__lte=datetime.date.today())

        return qs.difference(qs_passed).order_by("end_date")


class PassedEventListView(EventListViewBase):
    def get_queryset(self):
        qs = super().get_queryset()
        qs_passed = qs.filter(end_date__date__lte=datetime.date.today())
        return qs_passed.order_by("-end_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["passed"] = True
        return context
