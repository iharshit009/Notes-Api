from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Notes
from .serializers import NoteSerializer


class NoteList(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
