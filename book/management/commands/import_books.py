import csv
import os
from django.core.management.base import BaseCommand
from book.models import Book

class Command(BaseCommand):
    help = "Import books from CSV file."

    def handle(self, *args, **options):
        csv_file_path = os.path.join(
            os.path.dirname(__file__),
            "data/dummy_books.csv"
        )
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Book.objects.create(
                    title=row["title"],
                    author=row["author"],
                    description=row["description"],
                    inventory=row["inventory"]
                )
        self.stdout.write("Import completed.")