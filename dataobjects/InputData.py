class InputData:

    def __init__(self, available_days, books, libraries):
        self.available_days = available_days
        self.books = books
        self.libraries = libraries

    def __str__(self):
        return "available_days={}, books={}, libraries={}".format(self.available_days,
                                                                  [str(book) for book in self.books],
                                                                  [str(lib) for lib in self.libraries])
