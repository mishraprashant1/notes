from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone

from .forms import CreateNewNoteForm
from apps.notes.models.notes import Notes


class CreateNoteForm(LoginRequiredMixin, FormView):
    login_url = '/auth'
    template_name = 'create_note/new_note.html'
    form_class = CreateNewNoteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uuid = self.request.GET.get('id')
        if uuid:
            context['page_title'] = 'Update Note'
        else:
            context['page_title'] = 'Create Note'
        context['user_id'] = self.request.user
        return context

    def get_initial(self):
        uuid = self.request.GET.get('id')
        if uuid:
            note = Notes.objects.get(uuid=uuid)
            self.initial['title'] = note.title
            self.initial['note'] = note.content
        else:
            self.initial['title'] = None
            self.initial['note'] = None
        return super().get_initial()

    def form_valid(self, form):
        data = form.cleaned_data
        title = data['title']
        content = data['note']
        current_timestamp = timezone.now()

        uuid = self.request.GET.get('id', None)

        if uuid:
            note = Notes.objects.get(uuid=uuid)
            note.title = title
            note.content = content
            note.modified_at = current_timestamp
        else:
            note = Notes()
            note.user = self.request.user
            note.title = title
            note.content = content
            note.created_at = current_timestamp
            note.modified_at = current_timestamp
        note.save()

        return redirect('notes_index')
