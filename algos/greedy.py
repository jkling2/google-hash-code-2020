from algos.heuristics import sort_books_by_book_score_desc
from dataobjects.InputData import InputData
from dataobjects.Library import Library
import math


def score_lib_greedy(library, available_days):
    """
    greedy algorithm to score libraries
    :param Library library: the libraries to score
    :param int available_days: the days left
    :return: the score of the library
    :rtype: int
    """
    total_books_until_end = available_days * library.books_per_day
    if total_books_until_end < 0:
        return 0
    else:
        lib_score = 0
        for idx, book in enumerate(library.books):
            if idx >= total_books_until_end:
                break
            else:
                lib_score += book.score
        return lib_score


def score_lib_greedy_red_sign_up_time(library, available_days):
    """
    uses the greedy algorithm's score and applies the sign up time needed
    :param Library library: the libraries to score
    :param int available_days: the days left
    :return: the score of the library
    :rtype: int
    """
    return score_lib_greedy(library, available_days) / library.sign_up_days_needed


def score_greedy_total_books(library, available_days):
    """
    uses the greedy algorithm's score and applies the total amount of books
    :param Library library: the libraries to score
    :param int available_days: the days left
    :return: the score of the library
    :rtype: int
    """
    return score_lib_greedy(library, available_days) * len(library.books)


def score_greedy_used_books(library, available_days):
    """
    uses the greedy algorithm's score and applies the amount of used books
    :param Library library: the libraries to score
    :param int available_days: the days left
    :return: the score of the library
    :rtype: int
    """
    total_books_until_end = min((available_days - library.sign_up_days_needed) * library.books_per_day,
                                len(library.books))
    return score_lib_greedy(library, available_days) * total_books_until_end


def score_average_book_score(library, available_days):
    """
    determines the library score based on the average book score
    :param Library library: the libraries to score
    :param int available_days: the days left
    :return: the score of the library
    :rtype: int
    """
    lib_book_score = sum(list(map(lambda book: book.score, library.books)))
    total_books_until_end = (available_days - library.sign_up_days_needed) * library.books_per_day
    if total_books_until_end <= 0:
        return 0
    else:
        return lib_book_score / total_books_until_end


def score_using_book_occurrence(library, available_days, book_occurrences):
    """
    determines the library score based on the available occurrence of each book
    :param Library library: the libraries to score
    :param int available_days: the days left
    :param int[] book_occurrences: the available occurrences of each book
    :return: the score of the library
    :rtype: int
    """
    total_books_until_end = (available_days - library.sign_up_days_needed) * library.books_per_day
    if total_books_until_end < 0:
        return 0
    else:
        lib_score = 0
        for idx, book in enumerate(library.books):
            if idx >= total_books_until_end:
                break
            else:
                if book_occurrences[book.idx] <= 0:
                    return 0
                lib_score += (book.score / math.sqrt(book_occurrences[book.idx]))
        return lib_score


def determine_library_score(library, available_days, used_books_idx, book_occurrences):
    """
    determines the library score based on a certain algorithm
    :param Library library: the libraries to score
    :param int available_days: the days left
    :param bool[] used_books_idx: the indices of the books that were already used
    :param int[] book_occurrences: the available occurrences of each book
    :return: the score of the library
    :rtype: int
    """
    # remove used books
    library.books[:] = [book for book in library.books if not used_books_idx[book.idx]]
    return score_lib_greedy_red_sign_up_time(library, available_days, used_books_idx)


def greedy(input_data):
    """
    sort libraries by a score that uses the attributes provided by the input data (available days, sign up days
    needed and the library's books)
    :param InputData input_data : The input data
    :return: The libraries with contained books that are used for book registration
    :rtype: array of Library
    """
    available_days = input_data.available_days
    libraries = input_data.libraries
    # initialize array for used books to all false
    used_books_idx = [False for i in range(len(input_data.books))]
    # set up the initial occurrence of each book
    book_occurrences = [0 for i in range(len(input_data.books))]
    for library in libraries:
        for book in library.books:
            book_occurrences[book.idx] += 1
    # initialize array for used libraries to all false
    used_libraries_idx = [False for i in range(len(libraries))]
    # sort books in library by descending score
    libraries = list(map(lambda lib: sort_books_by_book_score_desc(lib), libraries))
    # initialize used libraries
    used_libraries = []
    while available_days > 0 and len(used_libraries) < len(libraries):
        max_lib_score = -1
        best_library = None
        # determine the best library at this point
        for library in libraries:
            if used_libraries_idx[library.idx]:
                continue
            library_score = determine_library_score(library, available_days, used_books_idx, book_occurrences)
            if library_score > max_lib_score:
                best_library = library
                max_lib_score = library_score
        # best library was found - update variables
        print("Available Days={}, Score={}".format(available_days, max_lib_score))
        used_libraries_idx[best_library.idx] = True
        total_books_until_end = (available_days - best_library.sign_up_days_needed) * best_library.books_per_day
        for idx, book in enumerate(best_library.books):
            book_occurrences[book.idx] -= 1
            if idx < total_books_until_end:
                used_books_idx[book.idx] = True
        available_days -= best_library.sign_up_days_needed
        used_libraries.append(best_library)
    return used_libraries
