from dataobjects.Book import Book
from dataobjects.Library import Library
from dataobjects.InputData import InputData

def readData(filePath):
    books = dict()
    libraries = []
    daysForScanning = 0
    with open(filePath, 'r') as f:
        lines = f.read().splitlines()
        first_line = lines[0].split(' ')
        daysForScanning = int(first_line[2])
        second_line = lines[1].split(' ')
        for idx, el in enumerate(second_line):
            books[idx] = Book(idx, int(el))
        for j in range(int(first_line[1])):
            lineIndex = 2 + (j * 2)
            libraries.append(readLibrary(books, j, lines[lineIndex].split(' '), lines[lineIndex + 1].split(' ')))

    return InputData(daysForScanning, books.values(), libraries);


def readLibrary(books, idx, first_line, second_line):
    booksInLibrary = [];
    for book in second_line:
        booksInLibrary.append(books[int(book)]);
    return Library(idx, int(first_line[1]), int(first_line[2]), booksInLibrary);
