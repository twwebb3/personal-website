
from django.urls import path
from .views import NotesPageView, DataSciencePageView


urlpatterns = [
    path('', NotesPageView.as_view(), name='notes'),
    path('data_science/', DataSciencePageView.as_view(), name='data_science'),
]
