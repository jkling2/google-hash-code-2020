import sys
import iopackage.writer as writer
import iopackage.reader as reader
import iopackage.readerOO as readerOO
import iopackage.writerOO as writerOO
import test.score as score
import algos.heuristics as heuristics
import algos.greedy as greedy
#import utils.submission as submission
#import algos.simple as simpleAlgo
#import algos.StupidGreedy as stupidAlgo
#import test.test as test

from dataobjects.Book import Book
from dataobjects.Library import Library
from dataobjects.InputData import InputData
from dataobjects.OutputData import OutputData

def main(file):
    inputFile = 'data/' + file + '.txt'
    outputFile = 'data/' + file + '.out'

    # read data
    print("Read Data")
    inputData = readerOO.readData(inputFile)

    # do the magic
    #result = inputData
    #result = simpleAlgo.simpleRestructure(inputData)
    #result = stupidAlgo.stupid_greedy(inputData)

    # write in as out
    # outputData = OutputData(inputData.libraries)
    print("Process Data")
    #outputData = OutputData(heuristics.sortHeuristicLibraryBook(inputData))
    outputData = OutputData(greedy.greedy(inputData))

    # write data to file
    print("Write Data")
    writerOO.writeData(outputFile, outputData)

    # score
    print("Score")
    total_score = score.score(inputData.availableDays, outputData, len(inputData.books))
    print("score={}".format(total_score))

    print("Done")
    # tests
    #test.testResult(inputData, result)


FILE_A = "a_example"
FILE_B = "b_read_on"
FILE_C = "c_incunabula"
FILE_D = "d_tough_choices"
FILE_E = "e_so_many_books"
FILE_F = "f_libraries_of_the_world"

def getFileNameFromLetter(letter):
    letter = letter.upper()
    if (letter == 'A'):
        return FILE_A
    elif (letter == 'B'):
        return FILE_B
    elif (letter == 'C'):
        return FILE_C
    elif (letter == 'D'):
        return FILE_D
    elif (letter == 'E'):
        return FILE_E
    elif (letter == 'F'):
        return FILE_F

import argparse
if __name__ == '__main__':
    file = ''
    argparser = argparse.ArgumentParser()
    argparser.add_argument('letter', type=str, default=None)
    args = argparser.parse_args()

    if args.letter:
        file = getFileNameFromLetter(args.letter)
        print("Processing {}".format(file))



    main(file)

    # zip the project and copy *.out files to ./submissions/submission-yyyy-mm-dd_hh-mm-ss/
    #submission.bundleSubmission('.')
