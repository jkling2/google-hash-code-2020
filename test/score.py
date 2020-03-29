from dataobjects.OutputData import OutputData


def calculate_score(available_days, output_data, book_count):
    """
    calculates the score of the provided output data considering the amount of days available
    :param int available_days : The number of days that are available for signing up books
    :param OutputData output_data : The output data that is used for score calculation
    :param int book_count : The number of different books
    :return: the calculated score
    """
    score = 0
    used_books = [False for i in range(book_count)]
    for lib in output_data.libraries:
        available_days -= lib.sign_up_days_needed
        books_per_library = available_days * lib.books_per_day
        for idx, book in enumerate(lib.books):
            if idx >= books_per_library:
                break
            if used_books[book.idx]:
                continue
            score += book.score
            used_books[book.idx] = True
    return score
