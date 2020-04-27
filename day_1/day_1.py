from typing import List
import numpy as np
from utils.read_input import read_input


def calculate_fuel(mass: int) -> int:
    module_fuels = []
    while np.floor(mass/3.0) - 2 > 0:
        mass = np.floor(mass/3.0) - 2
        module_fuels.append(mass)

    fuel = sum(module_fuels)
    return fuel


def total_fuel(module_masses: List[str]) -> int:
    total = 0
    for mass in module_masses:
        total += calculate_fuel(int(mass))

    return total


if __name__ == "__main__":
    input = read_input("/Users/rhiannonsteele/PycharmProjects/advent-of-code/day_1/input.txt")
    tot = total_fuel(input)
    print(tot)