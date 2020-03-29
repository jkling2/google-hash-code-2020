class Book:

    def __init__(self, book_idx, book_score):
        self.idx = book_idx
        self.score = book_score

    def __str__(self):
        return "Book=[idx={}, score={}]".format(self.idx, self.score)
