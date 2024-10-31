
from django.views.generic import TemplateView


class NotesPageView(TemplateView):
    template_name = 'notes.html'

class DataSciencePageView(TemplateView):
    template_name = 'data_science.html'

