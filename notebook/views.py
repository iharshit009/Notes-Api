from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.

from .models import Notes
from .serializers import NoteSerializer


def getNotes(request):
    data = Notes.objects.all()
    return render(request, 'notebook/display.html', {'notes': data})


def userNotes(request, pk=None):
    print(pk)
    data = Notes.objects.filter(author_id=pk)
    return render(request, 'notebook/user.html', {'notes': data})