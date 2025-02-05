from django.test import TestCase
from django.urls import reverse
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

class BookViewsTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Author",
            description="Description",
            inventory=5
        )

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view(self):
        response = self.client.get(reverse("book_detail", args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)

    def test_book_create_view(self):
        response = self.client.post(reverse("book_create"), {
            "title": "New Book",
            "author": "New Author",
            "description": "New Description",
            "inventory": 10
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title="New Book").exists())

    def test_book_update_view(self):
        response = self.client.post(reverse("book_update", args=[self.book.pk]), {
            "title": "Updated Title",
            "author": "Updated Author",
            "description": "Updated",
            "inventory": 3
        })
        self.book.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.book.title, "Updated Title")

    def test_book_delete_view(self):
        response = self.client.post(reverse("book_delete", args=[self.book.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
