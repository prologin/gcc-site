from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from urllib.parse import urlencode
from users.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import events, signup

from .forms import (
    EventSignupForm
)


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
                    "city": request.POST["city"], "zip_code": request.POST["zip_code"], "country": request.POST["country"]}
                
                form_answer = {"tshirt": request.POST["tshirt"], "allergies": request.POST["allergies"], "diet": request.POST["diet"], "learning": request.POST["learn"],
                            "programing": request.POST["programing"], "studies": request.POST["studies"], "association": request.POST["association"]},

                application = signup.Application.objects.create(
                    user=user,
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    dob=request.POST["dob"],
                    address=address,
                    event=event,
                    form_answer=form_answer
                )

                messages.success(
                    request,
                    "Votre candidature a été enregistré!"
                )

                return HttpResponseRedirect(reverse("events:home"))
        
        elif "submit-newsletter" in request.POST:
            # DO SOMETHING HERE ?

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
        return ctx

class ApplicationsView(LoginRequiredMixin, TemplateView):
    template_name = 'events/mes-candidatures.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['application_documents'] = signup.Application.objects.filter(user=self.request.user.id)
        return ctx
