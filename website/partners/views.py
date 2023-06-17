from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Partner

def partners_view(request):
    partners = Partner.objects.all()
    context = {'partners': partners}
    return render(request, 'partners/partners.html', context)

def partners_view_featured(request):
    partners = Partner.objects.filter(featured=True)
    context = {'partners': partners}
    return render(request, 'partners/featured_partners.html', context)

