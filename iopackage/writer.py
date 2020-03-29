from dataobjects.OutputData import OutputData


def write_data(output_file, output_data):
    """
    writes the provided output data to the output file considering a specific output format
    :param str output_file : The path to the file to which the output string is written
    :param OutputData output_data : The output data that is written
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
    file = open(output_file, "w")
    file.write("".join(output_lines))
    return output_lines
