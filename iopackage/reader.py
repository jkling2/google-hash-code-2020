from dataobjects.Book import Book
from dataobjects.Library import Library
from dataobjects.InputData import InputData


def read_data(file_path):
    """
    parses the data provided in the given file and stores it into the desired data structures
    :param str file_path: The path to the file that contains the input data to parse
    :return: the parsed input data
    """
    books = dict()
    libraries = []
    max_score = 0
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        first_line = lines[0].split(' ')
        # 1: <number of days> available
        days_for_scanning = int(first_line[2])
        # 2: calculate max score possible and store <book scores>
        second_line = lines[1].split(' ')
        for idx, el in enumerate(second_line):
            max_score += int(el)
            books[idx] = Book(idx, int(el))
        # 3: individual <libraries> contained
        num_of_libs = int(first_line[1])
        for lib_idx in range(num_of_libs):
            line_idx = 2 + (lib_idx * 2)
            libraries.append(read_library(books, lib_idx, lines[line_idx].split(' '), lines[line_idx + 1].split(' ')))
    print("Max score = {}".format(max_score))
    return InputData(days_for_scanning, books.values(), libraries)


def read_library(books, lib_idx, library_meta_data, contained_book_idxs):
    """
    parses the data given for a library.
    :param dict books : Dictionary that maps the book's score to its index
    :param int lib_idx : The index of the library to read
    :param str[] library_meta_data : The library's meta data: number of books, sign-up days needed, shippable books per day
    :param str[] contained_book_idxs : The different books indices that are contained in the library
    :return: the parsed library
    """
    books_in_library = []
    for book_idx in contained_book_idxs:
        books_in_library.append(books[int(book_idx)])
    sign_up_days_needed = int(library_meta_data[1])
    books_per_day = int(library_meta_data[2])
    return Library(lib_idx, sign_up_days_needed, books_per_day, books_in_library)
