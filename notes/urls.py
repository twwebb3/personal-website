
from django.urls import path
from .views import NotesPageView, DataSciencePageView, ProgrammingPageView, DataEngineeringPageView, PythonPageView
from .views import RstatsPageView


urlpatterns = [
    path('', NotesPageView.as_view(), name='notes'),
    path('data_science/', DataSciencePageView.as_view(), name='data_science'),
    path('programming/', ProgrammingPageView.as_view(), name='programming'),
    path('data_engineering/', DataEngineeringPageView.as_view(), name='data_engineering'),
    path('programming/python', PythonPageView.as_view(), name='python'),
    path('programming/rstats', RstatsPageView.as_view(), name='rstats'),
]
