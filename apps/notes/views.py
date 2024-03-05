"""View File"""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.notes.serializer import NoteSerializer
from apps.notes.models import Note
from apps.notes.constants import ApplicationMessages


class NoteViewSet(viewsets.ModelViewSet):
    """Notes Viewset"""
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(is_delete=False)
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

    def create(self, request):
        """Create Note"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve Note"""
        try:
            note = get_object_or_404(Note, pk=pk)
            serializer = self.get_serializer(note)
            return Response(serializer.data)
        except Note.DoesNotExist:
            error = {"error": ApplicationMessages.NOTE_NOT_FOUND}
            return Response(error, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Update Note Info."""
        try:
            note = get_object_or_404(Note, pk=pk)
            serializer = self.get_serializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Note.DoesNotExist:
            error = {"error": ApplicationMessages.NOTE_NOT_FOUND}
            return Response(error, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Delete Note"""
        try:
            note = get_object_or_404(Note, pk=pk)
            note.is_deleted = True
            note.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist:
            error = {"error": ApplicationMessages.NOTE_NOT_FOUND}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
