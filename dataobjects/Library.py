class Library:

    def __init__(self, library_idx, sign_up_days_needed, books_per_day, books):
        self.idx = library_idx
        self.sign_up_days_needed = sign_up_days_needed
        self.books_per_day = books_per_day
        self.books = books

    def __str__(self):
        return "Library=[idx={}, sign_up_days_needed={}, books_per_day={}, books={}]".format(self.idx,
                                                                                             self.sign_up_days_needed,
                                                                                             self.books_per_day,
                                                                                             [str(book) for book in
                                                                                              self.books])
