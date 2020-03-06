from algos.heuristics import sortBooksByBookScore
import math

def scoreLibGreedy(library, availableDays, used_books_idx):
    total_books_until_end = (availableDays - library.signUpDaysNeeded) * library.booksPerDay
    if (total_books_until_end < 0):
        return 0
    else:
        lib_score = 0
        for idx, book in enumerate(library.books):
            if (idx >= total_books_until_end):
                break
            else:
                lib_score += book.bookScore
        return lib_score
        #library.books = library.books[0:total_books_until_end]
        #return sum(list(map(lambda book: book.bookScore, library.books)))

def scoreLibGreedyRedSignUpTime(library, availableDays, used_books_idx):
    return scoreLibGreedy(library, availableDays, used_books_idx) / library.signUpDaysNeeded


def scoreLibSize(library, availableDays, used_books_idx):
    lib_score = scoreLibGreedy(library, availableDays, used_books_idx)
    return lib_score * len(library.books)

def scoreUsedBookSize(library, availableDays, used_books_idx):
    lib_score = scoreLibGreedy(library, availableDays, used_books_idx)
    total_books_until_end = min((availableDays - library.signUpDaysNeeded) * library.booksPerDay, len(library.books))
    return lib_score * total_books_until_end

def scoreLibSeparate(library, availableDays, used_books_idx):
    lib_book_score = sum(list(map(lambda book: book.bookScore, library.books)))
    total_books_until_end = (availableDays - library.signUpDaysNeeded) * library.booksPerDay
    if (total_books_until_end <= 0):
        return 0
    else:
        return lib_book_score / total_books_until_end

def scoreUsingBookOccurrence(library, availableDays, used_books_idx, book_occurences):
    # todo: save occurence of a book in used_book_idx and determine score based on 1/#occurrence
    total_books_until_end = (availableDays - library.signUpDaysNeeded) * library.booksPerDay
    if (total_books_until_end < 0):
        return 0
    else:
        lib_score = 0
        for idx, book in enumerate(library.books):
            if (idx >= total_books_until_end):
                break
            else:
                if (book_occurences[book.bookIndex] <= 0):
                    return 0
                lib_score += (book.bookScore / math.sqrt(book_occurences[book.bookIndex]))
        return lib_score

def determineLibraryScore(library, availableDays, used_books_idx, book_occurences):
    #remove used books
    library.books[:] = [book for book in library.books if not used_books_idx[book.bookIndex]]
    return scoreLibGreedyRedSignUpTime(library, availableDays, used_books_idx)


def greedy(input_data):
    # sort libraries by a score that uses available days, sign up days needed and the library's books
    available_days = input_data.availableDays
    libraries = input_data.libraries
    used_books_idx = [False for i in range(len(input_data.books))]
    book_occurences = [0 for i in range(len(input_data.books))]
    for lib in libraries:
        for book in lib.books:
            book_occurences[book.bookIndex] += 1
    used_libraries_idx = [False for i in range(len(libraries))]
    used_libraries = []
    count = 0
    libraries = list(map(lambda lib: sortBooksByBookScore(lib), libraries))
    while (available_days > 0 and count < len(libraries)):
        max_lib_score = -1
        used_library = None
        for lib in libraries:
            if used_libraries_idx[lib.idx]:
                continue
            library_score = determineLibraryScore(lib, available_days, used_books_idx, book_occurences)
            if library_score > max_lib_score:
                used_library = lib
                max_lib_score = library_score
        print("Available Days={}, Score={}".format(available_days, max_lib_score))
        used_libraries_idx[used_library.idx] = True
        total_books_until_end = (available_days - used_library.signUpDaysNeeded) * used_library.booksPerDay
        for idx, book in enumerate(used_library.books):
            book_occurences[book.bookIndex] -= 1
            if (idx < total_books_until_end):
                used_books_idx[book.bookIndex] = True
        #used_library.books = used_library.books[0:total_books_until_end]
        available_days -= used_library.signUpDaysNeeded
        count += 1
        used_libraries.append(used_library)

    return used_libraries

