from services.post.data import BOOK_CHOICES
from services.post.models import Book


def load_books():
    for book_id, book_name in BOOK_CHOICES:
        book_obj, created = Book.objects.get_or_create(id=book_id, defaults={'name': book_name})
        if created:
            print(f'Book {book_name} created.')
        else:
            print(f'Book {book_name} already exists.')
        print(f'Book object: {book_obj}')


load_books()
