
from django.views.generic import TemplateView


class NotesPageView(TemplateView):
    template_name = 'notes.html'
