class Bookstore(object):
    def __init__(self, name):
        self.name=name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def get_books(self):
        return self.books
    def search_books(self, title=None, author=None):
        results = []
        if author == None:
            for i, value in enumerate(self.books):
                if title.lower() in self.books[i].title.lower():
                    results.append(self.books[i])
            return results
        else:
            for i, value in enumerate(self.books):
                if author.name.lower() in self.books[i].author.name.lower():
                    results.append(self.books[i])
            return results

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.booklist = []
    
    def get_books(self):
        return self.booklist


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.booklist.append(self)