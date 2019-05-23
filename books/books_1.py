from datetime import datetime

class Book:

    def __init__(self, title):
        self.title = title
        self._author = None
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception('Authors must be of class type "Author"')

    @author.deleter
    def author(self):
        del self._author
    
    def __repr__(self):
        return self.title

class Author:
    
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    @property
    def inaccurate_age(self):
        return datetime.now().year - self.birthyear

b1 = Book('Harry Potter and the Philosophers Stone')
a1 = Author('J. K. Rowling', 1965)

