def readData (filePath):
	daysForScanning = 0
	bookScores = []
	with open(filePath, 'r') as f:
		lines = f.read().splitlines()
		first_line = lines[0].split(' ')
		daysForScanning = int(first_line[2])
		second_line = lines[1].split(' ')
		for book in second_line :
			bookScores.append(int(book))
		libraries = []
		for i in range(int(first_line[1])):
			lineIndex = 2 + (i * 2)
			libraries.append(readLibrary(lines[lineIndex].split(' '), lines[lineIndex+1].split(' ')))

	return [daysForScanning, bookScores, libraries]

def readLibrary(first_line, second_line):
	booksInLibrary = []
	for book in second_line:
		booksInLibrary.append(int(book))
	return [int(first_line[1]), int(first_line[2]), booksInLibrary]