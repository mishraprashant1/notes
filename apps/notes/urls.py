from django.urls import path
from .views import *

urlpatterns = [
    path('', NotesIndexView.as_view(), name='notes_index'),
    path('create-note/', CreateNoteForm.as_view(), name='create_note'),
    path('<uuid:note_uuid>/', NotesViewAjax.as_view(), name='note_content')
]
