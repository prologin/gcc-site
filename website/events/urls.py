from django.urls import include, path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path(
        "event-signup",
        views.HomePageView.as_view(http_method_names=["post"]),
        name="event_signup",
    ),
    path("review/", views.ReviewIndexView.as_view(), name="review"),
    path(
        "review/<int:year>/<int:event>",
        views.ApplicationsReviewView.as_view(),
        name="application_review",
    ),
    path("my-applications", views.ApplicationsView.as_view(), name="my_applications"),
]
