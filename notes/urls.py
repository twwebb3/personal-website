
from django.urls import path
from .views import NotesPageView

urlpatterns = [
    path('', NotesPageView.as_view(), name='notes'),  # Adjust as necessary
]
