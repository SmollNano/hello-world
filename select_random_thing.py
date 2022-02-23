import random
import csv


def select_random_from_list(in_list):
    # RNG = random.randint(0, len(in_list) - 1)
    # selected = in_list[RNG]
    return in_list[random.randint(0, len(in_list) - 1)][0]


def open_file(filepath):
    """
    Reads a csv file and returns a list

    :param filepath: path to the file
    :return: list of csv
    """
    out_list = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            out_list.append(line)

    return out_list
