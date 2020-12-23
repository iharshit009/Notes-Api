from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.

from .models import Notes
from .serializers import NoteSerializer


class NoteList(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class NoteCreate(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class NoteUpdate(generics.UpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class NoteDelete(generics.DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = Notes.objects.all()

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Notes.objects.filter(pk=pk)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
