"""Test-cases File"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.notes.models import Note


class NoteAPITestCases(TestCase):
    """Note API Testcases"""
    def setUp(self):
        self.client = APIClient()
        self.note1 = Note.objects.create(
            title="Note 1", description="Description of Note 1",
            status="DRAFT"
        )
        self.note2 = Note.objects.create(
            title="Note 2", description="Description of Note 2",
            status="PUBLISHED"
        )

    def test_list_notes(self):
        """List all note test-case"""
        response = self.client.get(reverse("note-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_note(self):
        """Create Note test-case"""
        data = {
            'title': 'Travel Note',
            'description': 'I am going to travel.'
        }
        response = self.client.post(reverse('note-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 3)

    def test_retrieve_note(self):
        """Retrieve Paticular Note data"""
        response = self.client.get(
            reverse('note-detail', kwargs={'pk': self.note1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Note 1")
        self.assertEqual(response.data['description'], "Description of Note 1")

    def test_update_note(self):
        """Update note test-case"""
        data = {
            'title': 'Updated Note',
            'description': 'Description of Updated Note'
        }
        response = self.client.put(
            reverse('note-detail', kwargs={'pk': self.note1.pk}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(pk=self.note1.pk).title, 'Updated Note')

    def test_delete_note(self):
        """Delete note test case"""
        response = self.client.delete(
            reverse('note-detail', kwargs={'pk': self.note1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 1)
