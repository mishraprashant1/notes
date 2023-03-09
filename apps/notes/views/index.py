from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.notes.models import Notes


class NotesIndexView(LoginRequiredMixin, ListView):
    login_url = '/auth'
    template_name = 'notes_index/notes_index.html'
    model = Notes
    paginate_by = 3

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user).order_by('-modified_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Notes'
        context['user_id'] = self.request.user
        return context
