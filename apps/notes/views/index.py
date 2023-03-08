from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesIndex(LoginRequiredMixin, TemplateView):
    login_url = '/auth'
    template_name = 'notes_index/notes_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Notes'
        print('Something here ----->', self.request)
        context['user_id'] = self.request.user
        return context
