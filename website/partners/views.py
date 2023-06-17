from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


from django.http import HttpResponse
from .models import Partner


class partners_view(ListView):
    model = Partner

def partners_view(request):
    partners = Partner.objects.all()
    context = {'partners': partners}
    return render(request, 'partners/partners.html', context)

