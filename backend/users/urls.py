from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
  path('accountinformationsview', views.AccountInformationsView.as_view(), name='AccountInformationsView')
]
