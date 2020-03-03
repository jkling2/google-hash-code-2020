from algos.heuristics import sortBooksByBookScore


def determineLibraryScore(library, availableDays):
    score = library.idx
    return score


def greedy(input_data):
    # sort libraries by a score that uses available days, sign up days needed and the library's books
    available_days = input_data.availableDays
    libraries = input_data.libraries.copy()
    #used_books_idx = [False for i in range(len(input_data.books))]
    used_libraries_idx = [False for i in range(len(libraries))]
    used_libraries = []
    count = 0
    while (available_days > 0 and count < len(libraries)):
        max_lib_score = -1
        used_library = None
        for lib in libraries:
            if used_libraries_idx[lib.idx]:
                continue
            library_score = determineLibraryScore(lib, available_days)
            if library_score > max_lib_score:
                used_library = lib
                max_lib_score = library_score

        used_libraries_idx[used_library.idx] = True
        available_days -= used_library.signUpDaysNeeded
        count += 1
        sortBooksByBookScore(used_library)
        used_libraries.append(used_library)

    return used_libraries

