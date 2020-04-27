from typing import List


def read_input(file_path: str) -> List[str]:
    """
    reads an input text file line by line and gives a list of strings
    :param file_path: The full file path to be read in
    :return: a list of strings
    """

    f = open(file_path, 'r')
    read_data = f.readlines()
    f.close()
    read_data = [string.strip('\n') for string in read_data]

    return read_data


def read_wires(file_path: str) -> List[List[str]]:
    """
    reads an input wires text file (i.e. for day 3) and returns list of lists. Each wire is its own list in the list.
    :param file_path: The full file path to be read in
    :return: A list of lists of strings
    """
    f = open(file_path)
    read_data = f.readlines()
    wires = [0] * len(read_data)

    for num in range(0, len(read_data)):
        wires[num] = read_data[num].split(',')

    return wires

if __name__ == "__main__":
    read_wires("/Users/rhiannonsteele/PycharmProjects/advent-of-code/day_3/input.txt")
