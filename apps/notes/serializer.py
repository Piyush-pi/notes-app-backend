"""Serializer File"""
from rest_framework import serializers
from apps.notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Note serializer"""
    class Meta:
        """Meta Class"""
        model = Note
        fields = "__all__"
