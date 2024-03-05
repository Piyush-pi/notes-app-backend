"""Django Admin File"""
from django.contrib import admin
from apps.notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Note admin class"""
    list_display = ["id", "title", "status"]
