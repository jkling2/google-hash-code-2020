
def sortByBookScore(book):
    return book.bookScore

def sortByLibraryScore(library):
    return sum(map(lambda book: book.bookScore, library.books))

def sortHeuristicLibraryBook(input_data):
    libraries = input_data.libraries
    libraries.sort(key = sortByLibraryScore, reverse = True)
    for lib in libraries:
        sortBooksByBookScore(lib)
    return libraries

def sortHeuristicBooks(input_data):
    libraries = input_data.libraries
    for lib in libraries:
        sortBooksByBookScore(lib)
    return libraries

def sortBooksByBookScore(library):
    books = library.books
    books.sort(key = sortByBookScore, reverse = True)
    return library
