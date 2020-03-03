import sys

def write(output_file, list):
    outputLines = []

    numberOfLibs = len(list)

    # 1: <number of libraries>
    outputLines.append(str(numberOfLibs) + "\n")
    # 2: 
    #outputLines.append("\n")

    for lib in list:
        libIndex = lib[0]
        bookList = lib[1]
        numberOfBooks = len(bookList)

        # 3: <Library Index> <Number of Books>
        outputLines.append(str(libIndex) + " " + str(numberOfBooks) + "\n")
        # 4:
        #outputLines.append("\n")

        bookLine = ""
        for book in bookList:
            bookLine += str(book) + " "

        bookLine = bookLine[:-1]
        
        # 5: <Array of Books>
        outputLines.append(bookLine + "\n")

        # 6: 
        #outputLines.append("\n")

    
    file = open(output_file, "w")
    file.write("".join(outputLines))

if __name__ == "__main__":
    write('test.out', [[1, [5, 2, 3]], [0, [0, 1, 2, 3, 4]]])
