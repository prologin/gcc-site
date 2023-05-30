from django.urls import include, path

from . import views

app_name = "events"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('review/', views.ReviewIndexView.as_view(), name="review"),
    path('review/<int:year>/<int:event>',
         views.ApplicationsReviewView.as_view(), name="application_review")
]
