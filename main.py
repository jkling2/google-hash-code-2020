import argparse
import iopackage.reader as reader
import iopackage.writer as writer
import test.score as score
import algos.greedy as greedy
from dataobjects.OutputData import OutputData


def main(file_name):
    input_file = 'data/' + file_name + '.txt'
    output_file = 'data/' + file_name + '.out'

    # read data
    print("Read Data")
    input_data = reader.read_data(input_file)

    # write in as out
    print("Process Data")
    # outputData = OutputData(inputData.libraries)
    # outputData = OutputData(heuristics.sortHeuristicLibraryBook(inputData))
    output_data = OutputData(greedy.greedy(input_data))

    # write data to file
    print("Write Data")
    writer.write_data(output_file, output_data)

    # score
    print("Score")
    total_score = score.calculate_score(input_data.available_days, output_data, len(input_data.books))
    print("score={}".format(total_score))
    print("Done")


FILE_A = "a_example"
FILE_B = "b_read_on"
FILE_C = "c_incunabula"
FILE_D = "d_tough_choices"
FILE_E = "e_so_many_books"
FILE_F = "f_libraries_of_the_world"


def get_file_name_from_letter(letter):
    letter = letter.upper()
    if letter == 'A':
        return FILE_A
    elif letter == 'B':
        return FILE_B
    elif letter == 'C':
        return FILE_C
    elif letter == 'D':
        return FILE_D
    elif letter == 'E':
        return FILE_E
    elif letter == 'F':
        return FILE_F


if __name__ == '__main__':
    file = ''
    argparser = argparse.ArgumentParser()
    argparser.add_argument('letter', type=str, default=None)
    args = argparser.parse_args()

    if args.letter:
        file = get_file_name_from_letter(args.letter)
        print("Processing {}".format(file))

    main(file)
