
def writeData(output_file, output_data):
    outputLines = []

    numberOfLibs = len(output_data.libraries)

    # 1: <number of libraries>
    outputLines.append(str(numberOfLibs) + "\n")

    for lib in output_data.libraries:
        numberOfBooks = len(lib.books)

        # 2: <Library Index> <Number of Books>
        outputLines.append(str(lib.idx) + " " + str(numberOfBooks) + "\n")

        bookLine = ""
        for book in lib.books:
            bookLine += str(book.bookIndex) + " "

        bookLine = bookLine[:-1]

        # 3: <Array of Books>
        outputLines.append(bookLine + "\n")

    file = open(output_file, "w")
    file.write("".join(outputLines))
    return outputLines

