from django.test import TestCase
from book.models import Book

class BookModelTests(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="Test Title",
            author="Test Author",
            description="Test Description",
            inventory=5
        )
        self.assertEqual(book.title, "Test Title")

    def test_str_method(self):
        book = Book.objects.create(
            title="String Method Test",
            author="Test Author",
            description="Test",
            inventory=1
        )
        self.assertEqual(str(book), "String Method Test")
