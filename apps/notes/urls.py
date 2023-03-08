from django.urls import path
from .views import *

urlpatterns = [
    path('', NotesIndex.as_view(), name='notes_index'),
]
