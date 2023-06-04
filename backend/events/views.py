from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, QueryDict
from django.urls import reverse
from django.contrib import messages
from urllib.parse import urlencode
from users.models import User

from .models import events, signup

from .forms import (
    EventSignupForm
)


class HomePageView(TemplateView):
    template_name = "events/home.html"
    form_class = EventSignupForm

    def post(self, request, *args, **kwargs):
        application_form = EventSignupForm(request.POST)
        print(request.POST)
        if "submit-application" in request.POST:
            print(request.user)
            event = events.Event.objects.get(id=request.POST["event-id"])
            print(event)
            user = User.objects.get(id=request.user.id)
            # dict_post ={
            #     "user": user,
            #     "first_name": request.POST["first_name"],
            #     "last_name": request.POST["last_name"],
            #     "dob": request.POST["dob"],
            #     "address": {
            #         "city": request.POST["city"],
            #         "zip_code": request.POST["zip_code"],
            #         "country": request.POST["country"]
            #     },
            #     "event": event,
            #     "form_answer": [
            #         "tshirt": request.POST["tshirt"],
            #         "allergies": request.POST["allergies"],
            #         "diet": request.POST["diet"],
            #         "learn": request.POST["learn"],
            #         "programing": request.POST["programing"],
            #         "studies": request.POST["studies"],
            #         "association": request.POST["association"]
            #     ],
            # }
            # new_request_post = urlencode(dict_post)
            # new_request_post = QueryDict.fromkeys(
            #     ["user", "first_name", "last_name", "dob",
            #         "address", "event", "form_answer"],
            #     value=[user,
            #            request.POST["first_name"],
            #            request.POST["last_name"],
            #            request.POST["dob"],
            #            {
            #                "city": request.POST["city"],
            #                "zip_code": request.POST["zip_code"],
            #                "country": request.POST["country"]
            #            },
            #            event,
            #            {
            #                "tshirt": request.POST["tshirt"],
            #                "allergies": request.POST["allergies"],
            #                "diet": request.POST["diet"],
            #                "learn": request.POST["learn"],
            #                "programing": request.POST["programing"],
            #                "studies": request.POST["studies"],
            #                "association": request.POST["association"]
            #            }])
            # print(new_request_post)
            messages.success(
                request,
                "Test"
            )

        return HttpResponseRedirect(reverse("events:home"))

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['open_events'] = events.Event.objects.get_open_events()
        ctx['form'] = EventSignupForm
        return ctx


class ReviewIndexView(TemplateView):
    template_name = 'events/application/index.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['open_events'] = events.Event.objects.get_open_events()
        ctx['events'] = events.Event.objects.get_visible_events()
        return ctx


class ApplicationsReviewView(TemplateView):
    template_name = 'events/application/review.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        print(kwargs)
        ctx["applications"] = signup.Application.objects.get_applicants(
            kwargs['event'])
        return ctx
