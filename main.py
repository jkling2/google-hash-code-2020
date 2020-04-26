import argparse
import iopackage.reader as reader
import iopackage.writer as writer
import test.score as score
import algos.greedy as greedy
from dataobjects.OutputData import OutputData
from dataobjects.Algo import Algo
from enum import Enum


def main(file_name, algo):
    input_file = 'data/' + file_name.value + '.txt'
    output_file = 'data/' + file_name.value + '.out'

    # read data
    print("Read Data")
    input_data = reader.read_data(input_file)

    # write in as out
    print("Process Data")
    # outputData = OutputData(inputData.libraries)
    # outputData = OutputData(heuristics.sortHeuristicLibraryBook(inputData))
    output_data = OutputData(greedy.greedy(input_data, algo))

    # write data to file
    print("Write Data")
    writer.write_data(output_file, output_data)

    # score
    print("Score")
    total_score = score.calculate_score(input_data.available_days, output_data, len(input_data.books))
    print("score={}".format(total_score))
    print("Done")


class File(Enum):
    A = "a_example"
    B = "b_read_on"
    C = "c_incunabula"
    D = "d_tough_choices"
    E = "e_so_many_books"
    F = "f_libraries_of_the_world"


if __name__ == '__main__':
    file = ''
    algo = 0
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--file', type=str, default=None)
    argparser.add_argument('--algo', type=int, default=0)
    args = argparser.parse_args()

    if args.file and args.algo:
        file = File[args.file]
        algo = Algo(args.algo)
        print("Processing {} ({}) with algo {}".format(file.value, file, algo))

    main(file, algo)
