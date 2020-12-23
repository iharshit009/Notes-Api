from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>/', views.NoteDetail.as_view()),
    path('delete/<int:pk>/', views.NoteDelete.as_view()),
    path('update/<int:pk>/', views.NoteUpdate.as_view()),
    path('postNote/', views.NoteCreate.as_view()),
]
