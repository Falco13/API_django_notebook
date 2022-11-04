from django.urls import path
from api.views import *

urlpatterns = [
    path('notes/', NoteListView.as_view()),
    path('notes/<int:pk>', NoteDetailView.as_view(), name='notes-detail'),
]
