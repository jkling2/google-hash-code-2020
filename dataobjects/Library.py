class Library:

    def __init__(self, library_idx, sign_up_days_needed, booksPerDay, books):
        self.idx = library_idx
        self.signUpDaysNeeded = sign_up_days_needed
        self.booksPerDay = booksPerDay
        self.books = books

    def __str__(self):
        return "Library=[idx={}, signUpDaysNeeded={}, booksPerDay={}, books={}]".format(self.idx, self.signUpDaysNeeded, self.booksPerDay, [str(book) for book in self.books])