from dataobjects.OutputData import OutputData
from datetime import datetime


def write_data(output_file_name, output_data, score):
    """
    writes the provided output data to the output file considering a specific output format
    :param str output_file_name : The path to the file to which the output string is written
    :param OutputData output_data : The output data that is written
    :param int score : The score of the output
    :return: the string array containing the output lines
    """
    output_lines = []
    number_of_libs = len(output_data.libraries)
    # 1: <number of libraries>
    output_lines.append(str(number_of_libs) + "\n")
    for lib in output_data.libraries:
        number_of_books = len(lib.books)
        # 2: <Library Index> <Number of Books>
        output_lines.append(str(lib.idx) + " " + str(number_of_books) + "\n")
        book_line = ""
        for book in lib.books:
            book_line += str(book.idx) + " "
        book_line = book_line[:-1]
        # 3: <Array of Books>
        output_lines.append(book_line + "\n")
    # current date and time
    now = datetime.now().timestamp()
    file = open("data/output/" + str(now) + "-" + str(score) + "-" + output_file_name + '.out', "w")
    file.write("".join(output_lines))
    return output_lines
