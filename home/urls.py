
from django.urls import path
from .views import HomePageView, ProfilePageView, NotesPageView, AppsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("notes/", NotesPageView.as_view(), name="notes"),
    path("apps/", AppsPageView.as_view(), name="apps"),
]
