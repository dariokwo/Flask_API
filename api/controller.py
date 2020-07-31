# Controller Methods to control API interactions with database
# You can add more middleware here as you see fit

from api.models import Book
from api.helpers import *


class BookController:
    """
    This is a general controller for the books
    You can pretty much cache data here if you want
    """

    def __self__(self):
        pass

    def db_get_book(self, book_id):
        return Book.query.filter_by(id=book_id).first()

    def db_get_all_books(self):
        return Book.query.all()

    def db_add_book(self, data):
        book = Book()
        book.set_from_json(book_data)
        db.session.add(book)
        db.session.commit()

    def handle_put(self, book_id, data):
        pass

    def db_delete_book(self, book_id):
        book = Book.query.filter_by(id=book_id).delete()
        db.session.commit()
        return book
