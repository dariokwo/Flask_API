def map_book_to_dict(book):
    """ 
    Convert Book data into key-value pairs matching JSON string 
    to be returned via HTTP GET
    :return: diction of dict matching HTTP GET response JSON string
    """
    return {
        "book_id": book.id,
        "book_name": book.name,
        "book_author": book.author,
        "book_quantity": book.quantity,
        "book_price": book.price,
        "create_at": book.date_created,
        "latest_update": book.last_modified,
    }


def map_dict_to_book_format(json):
    """
    Map a dictionary keys to Books db keys
    :return: new dict with keys matching book columnns
    """
    res = {}
    fields_mapping = [
        ("book_id", "id"),
        ("book_name", "name"),
        ("book_author", "author"),
        ("book_quantity", "quantity"),
        ("modified_on", "last_modified"),
        ("book_price", "price"),
        ("create_at", "date_created"),
    ]

    for key, col in fields_mapping:
        if key in json:
            res[col] = json[key]

    # new dict
    return res
