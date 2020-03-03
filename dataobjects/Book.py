class Book:

    def __init__(self, bookIndex, bookScore):
        self.bookIndex = bookIndex
        self.bookScore = bookScore

    def toString(self):
        return "Book=[idx={}, score={}]".format(self.bookIndex, self.bookScore)

    def __str__(self):
        return "Book=[idx={}, score={}]".format(self.bookIndex, self.bookScore)
