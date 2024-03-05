"""View File"""
from rest_framework import viewsets
from apps.notes.serializer import NoteSerializer
from apps.notes.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    """Notes Viewset"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # def get_queryset(self):
    #     queryset = Note.objects.all()
    #     title = self.request.query_params.get('title', None)
    #     if title is not None:
    #         queryset = queryset.filter(title=title)
    #     return queryset
