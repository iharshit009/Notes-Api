from django.urls import path
from . import views

urlpatterns = [
    path('GET/notes/', views.NoteList.as_view()),
    path('GET/note/<int:pk>/', views.NoteDetail.as_view()),
    path('DELETE/note/<int:pk>/', views.NoteDelete.as_view()),
    path('PUT/note/<int:pk>/', views.NoteUpdate.as_view()),
    path('POST/note/', views.NoteCreate.as_view()),
]
