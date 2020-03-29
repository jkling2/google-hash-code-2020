def __sort_by_book_score(book):
    return book.score


def __sort_by_library_score(library):
    return sum(map(lambda book: book.score, library.books))


def sort_books_by_book_score_desc(library):
    books = library.books
    books.sort(key=__sort_by_book_score, reverse=True)
    return library
