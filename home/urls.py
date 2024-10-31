
from django.urls import path
from .views import HomePageView, ProfilePageView, AppsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("apps/", AppsPageView.as_view(), name="apps"),
]
