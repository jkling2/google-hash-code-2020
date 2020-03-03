

def score(available_days, output_data, book_count):
    score = 0
    used_books = [False for i in range(book_count)]
    for lib in output_data.libraries:
        available_days -= lib.signUpDaysNeeded
        booksPerLibrary = available_days * lib.booksPerDay
        for idx, book in enumerate(lib.books):
            if idx >= booksPerLibrary:
                break
            if used_books[book.bookIndex]:
                continue
            score += book.bookScore
            used_books[book.bookIndex] = True

    return score