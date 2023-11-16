import datetime

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from applications.forms import EventApplicationForm
from applications.models import APPLICATION_STATUS, Application
from events.models import Event
from partners.models import Partner


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
        ctx["form"] = EventApplicationForm

        ctx["partners_avant"] = Partner.objects.filter(status="Promoted")
        ctx["partners_financement"] = Partner.objects.filter(
            status="Financing"
        )
        ctx["partners_accueil"] = Partner.objects.filter(status="Welcoming")

        ctx.update(APPLICATION_STATUS)
        return ctx


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
        ctx.update(APPLICATION_STATUS)
        return ctx


class ApplicationsReviewView(PermissionRequiredMixin, TemplateView):
    permission_required = "users.can_view_applications"
    template_name = "events/application/review.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["applications"] = Application.objects.get_applicants(
            kwargs["event"]
        )
        ctx.update(APPLICATION_STATUS)
        return ctx


class EventListViewBase(ListView):
    model = Event
    template_name = "events/event_list_page.html"
    # Show 5 elements per page
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EventApplicationForm
        context["passed"] = False
        return context


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
