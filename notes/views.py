
from django.views.generic import TemplateView


class NotesPageView(TemplateView):
    template_name = 'notes.html'

class DataSciencePageView(TemplateView):
    template_name = 'data_science.html'

class ProgrammingPageView(TemplateView):
    template_name = 'programming.html'

class DataEngineeringPageView(TemplateView):
    template_name = 'data_engineering.html'

class PythonPageView(TemplateView):
    template_name = 'programming/python.html'

class RstatsPageView(TemplateView):
    template_name = "programming/rstats.html"

class GitPageView(TemplateView):
    template_name = "programming/git.html"

