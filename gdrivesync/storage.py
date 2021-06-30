from tinydb import Query, TinyDB, where
db = TinyDB('db.json')

def get_books_dict():
    return db.all()

def add_or_update(id, name):
    Book = Query()
    search_result = db.search(Book.id == id)
    assert(len(search_result) <= 1)
    if not search_result:
        db.insert({'id': id, 'name': name})
        return True
    else:
        db.update({'name': name}, Book.id == id)
        return False

def remove_entry(id):
    db.remove(where('id') == id)

