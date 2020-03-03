import numpy as np

def testResult(inputData, outputData):
    days = int(inputData[0])
    bookScores = inputData[1]
    libData = inputData[2]

    signUpTimes = np.empty(len(libData), dtype=int)
    shippingTimes = np.empty(len(libData), dtype=int)
    booksPerLibs = np.empty(len(libData), dtype=list)
    for index, lib in enumerate(libData):
        signUpTimes[index] = lib[0]
        shippingTimes[index] = lib[1]
        booksPerLibs[index] = lib[2]
    
    registeredLibsAtTime = getRegisteredLibsAndTimes(signUpTimes, outputData, days)

    registeredBooksPerLib = getRegisteredBooksPerLib(outputData, registeredLibsAtTime, shippingTimes, days)
    
    score = 0
    for books in list(registeredBooksPerLib.values()):
        for book in books:
            score += bookScores[book]
    print(score)
    resultLibsAndBooks = outputData
  #  libraryHasBooks(booksPerLibs, resultLibsAndBooks)
    hasDuplicatedLibs(list(registeredLibsAtTime.values()))

def getRegisteredBooksPerLib(outputData, registeredLibsAtTime, shippingTimes, days):
    registeredBooksPerLib = {}
    for libData in outputData:
        libId = libData[0]
        bookList = libData[1]
        date = registeredLibsAtTime.get(libId)
        currentShippingTime = shippingTimes[libId]
        registeredBooks = []
        for book in bookList:
            date += currentShippingTime
            if date < days:
                registeredBooks.append(book)
            else:
                break
        registeredBooksPerLib.update({libId : registeredBooks})
    return registeredBooksPerLib

def getRegisteredLibsAndTimes(signUpTimes, outputData, days):
    registeredLibsAtTime = {}
    currentTime = 0
    for index, lib in enumerate(outputData):
        libId = lib[0]
        neededTime = signUpTimes[libId]
        currentTime += neededTime
        if currentTime >= days:
            break
        registeredLibsAtTime.update({libId : currentTime})
    return registeredLibsAtTime

def hasDuplicatedLibs(libs):
    libSet = set()
    hasDuplicates = False
    for lib in libs:
        if lib in libSet:
            hasDuplicates = True
            print("duplicated lib registration for: " + lib)
        libSet.add(lib)
    return hasDuplicates

def libraryHasBooks(booksPerLibs, resultLibsAndBooks):
    hasBooks = True
    for currentBooks in resultLibsAndBooks:
        currentBookSet = set(booksPerLibs[currentBooks[0]])
        for currentBook in currentBooks:
            if currentBook not in currentBookSet:
                print(currentBookSet + "is not in libray " + currentBooks[0])
                hasBooks = False
    return hasBooks