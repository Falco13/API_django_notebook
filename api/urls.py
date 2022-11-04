from django.urls import path
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls

# for more trim urls
'''
notes_list = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

notes_detail = NoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
'''

# for another urls
'''
urlpatterns = [
    path('notes/', notes_list),
    path('notes/<int:pk>', notes_detail, name='notes-detail'),

    # # # for class APIView and functions
    # path('notes/', NoteListView.as_view()),
    # path('notes/<int:pk>', NoteDetailView.as_view(), name='notes-detail'),
]
'''
