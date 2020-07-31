from flask import request, jsonify, make_response
from api import app, db
from api.models import Book
from api.helpers import *

# Handling HTTP request and response(All in this file)
# Alternatively, you can import the BookController from the controller class
# And use map these API end points to their respective methods in the BookController object


# GET one resource with the provided id
@app.route("/books/<int:book_id>")
def one_book(book_id):
    # Get resource from database
    book = Book.query.filter_by(id=book_id).first()
    if book is None:  # If Resource is not found, respond with an error message
        return make_response(jsonify({"status": "Not Found"}), 404)

    # Respond with the resource data
    return make_response(jsonify(map_book_to_dict(book)), 200)


# GET all resources (aka books)
@app.route("/books/")
def all_books():
    books = Book.query.all()  # Get all from table

    res = []  # Generate a list of all resources
    for book in books:  # Map all resources to correct format
        res.append(map_book_to_dict(book))

    # Respond with the resources data
    return make_response(jsonify(res), 200)


# POST (aka Add new book)
@app.route("/books/", methods=["POST"])
def add_book():
    try:
        # Request must be json
        if request.is_json:
            book_data = request.get_json()

            # Book name and author are required fields
            if book_data.get("book_name") and book_data.get("book_author"):

                # Create and add book to the database
                book = Book()
                book.name = book_data.get("book_name")
                book.author = book_data.get("book_author")
                if book_data.get("book_price"):
                    book.price = book_data.get("book_price")
                if book_data.get("book_quantity"):
                    book.price = book_data.get("book_quantity")

                db.session.add(book)
                db.session.commit()

                return make_response(jsonify({"status": "success"}), 201)
    except Exception as ex:
        print(ex)

    return make_response(jsonify({"status": "failed"}), 422)


# PATCH (update book info by id)
@app.route("/books/<int:book_id>", methods=["PATCH"])
def update_book(book_id):
    # Make sure the resource exits
    book = Book.query.filter_by(id=book_id).first()
    if book:
        # make sure json data exist for updating the resource
        data = request.get_json()
        if data:
            data = map_json_to_book(data)
            if data:
                book = Book.query.filter_by(id=book_id).update(data)
                db.session.commit()
                return make_response(jsonify({"status": "success"}), 200)

        return make_response(jsonify({"status": "failed"}), 400)
    return make_response(jsonify({"status": "Not Found"}), 404)


# PUT (Add new book if doesn't exist, or else update)
@app.route("/books/<int:book_id>", methods=["PUT"])
def replace_book(book_id):
    # implementations for put method goes here

    pass


# DELETE (delete book by id)
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete(book_id):
    book = Book.query.filter_by(id=book_id).delete()
    db.session.commit()

    if book:  # It's deleted
        return make_response(jsonify({"status": "Deleted"}), 204)

    # Resource not found
    return make_response(jsonify({"status": "Not Found"}), 404)


# Those are the most common HTTP request METHODS used when creating an API
# You can obviously research the rest and decide if you need to implement them
#

# Invalid routes
@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({"status": "Not Allowed"}), 405)
