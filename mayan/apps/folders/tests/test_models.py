from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase

from documents.models import DocumentType
from documents.tests import TEST_DOCUMENT_PATH, TEST_DOCUMENT_TYPE
from user_management.tests.literals import (
    TEST_ADMIN_EMAIL, TEST_ADMIN_PASSWORD, TEST_ADMIN_USERNAME
)

from ..models import Folder

from .literals import TEST_FOLDER_LABEL


class FolderTestCase(TestCase):
    def setUp(self):
        self.document_type = DocumentType.objects.create(
            label=TEST_DOCUMENT_TYPE
        )

        with open(TEST_DOCUMENT_PATH) as file_object:
            self.document = self.document_type.new_document(
                file_object=file_object
            )

        self.user = get_user_model().objects.create_superuser(
            username=TEST_ADMIN_USERNAME, email=TEST_ADMIN_EMAIL,
            password=TEST_ADMIN_PASSWORD
        )

    def tearDown(self):
        self.document_type.delete()

    def test_folder_creation(self):
        folder = Folder.objects.create(label=TEST_FOLDER_LABEL)

        self.assertEqual(Folder.objects.all().count(), 1)
        self.assertEqual(list(Folder.objects.all()), [folder])

    def test_addition_of_documents(self):
        folder = Folder.objects.create(label=TEST_FOLDER_LABEL)
        folder.documents.add(self.document)

        self.assertEqual(folder.documents.count(), 1)
        self.assertEqual(list(folder.documents.all()), [self.document])

    def test_addition_and_deletion_of_documents(self):
        folder = Folder.objects.create(label=TEST_FOLDER_LABEL)
        folder.documents.add(self.document)

        self.assertEqual(folder.documents.count(), 1)
        self.assertEqual(list(folder.documents.all()), [self.document])

        folder.documents.remove(self.document)

        self.assertEqual(folder.documents.count(), 0)
        self.assertEqual(list(folder.documents.all()), [])
