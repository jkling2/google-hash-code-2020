class InputData:

    def __init__(self, availableDays, books, libraries):
        self.availableDays = availableDays
        self.books = books
        self.libraries = libraries

    def __str__(self):
        return "availableDays={}, books={}, libraries={}".format(self.availableDays, [str(book) for book in self.books], [str(lib) for lib in self.libraries])

