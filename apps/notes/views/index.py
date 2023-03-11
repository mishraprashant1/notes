from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from apps.notes.models import Notes


class NotesIndexView(LoginRequiredMixin, ListView):
    login_url = '/auth'
    template_name = 'notes_index/notes_index.html'
    model = Notes
    paginate_by = 30

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user).order_by('-modified_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Notes'
        context['user_id'] = self.request.user
        return context


class NotesViewAjax(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        note_uuid = kwargs['note_uuid']
        try:
            note = Notes.objects.get(uuid=note_uuid)

            data = dict()
            data['success'] = False
            if request.user == note.user:
                data['title'] = note.title
                data['content'] = note.content
                data['created_at'] = note.created_at
                data['success'] = True
            return JsonResponse(data)
        except:
            data = dict()
            data['success'] = False
            return JsonResponse(data)
