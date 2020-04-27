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


if __name__ == "__main__":
    read_input("/Users/rhiannonsteele/PycharmProjects/advent-of-code/day_1/input.txt")
