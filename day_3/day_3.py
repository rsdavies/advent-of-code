from typing import List
from utils.read_input import read_wires


def get_positions(wire):
    """
    Gives the x, y position of a wire after each instruction
    :param wire: the wire instructions
    :return: x, y. Assuming wire starts at 0, 0
    """
    x = 0
    y = 0
    positions = [(0, 0)]

    for instruction in wire:
        direction = instruction[0]
        dist = int(instruction[1:])
        if direction == "R":
            for pos in range(1, dist+1):
                positions.append((x + pos, y))
            x += dist
        elif direction == "L":
            for pos in range(1, dist+1):
                positions.append((x - pos, y))
            x -= dist
        elif direction == "U":
            for pos in range(1, dist + 1):
                positions.append((x, y + pos))
            y += dist
        elif direction == "D":
            for pos in range(1, dist + 1):
                positions.append((x, y - pos))
            y -= dist
        else:
            raise ValueError("Direction not recognised")

    return positions


def manhattan_distance(x: int, y: int) -> int:
    return abs(x) + abs(y)


def distance(wires) -> int:
    """
    Takes the wires and finds the manhattan distance of the closest intersection to (0,0)
    :param wires: a list of lists of wires
    :return: the Manhattan distance to the central port of the closest cross
    """

    wire_0_pos = get_positions(wires[0])
    wire_1_pos = get_positions(wires[1])

    # find intersections
    intersections = list(set(wire_0_pos).intersection(set(wire_1_pos)))
    # ignore the 0,0 intersect
    intersections.remove((0, 0))
    m_distances = [manhattan_distance(x, y) for x, y in intersections]


    return min(m_distances)


def steps(wires) -> int:
    """
    Takes the wires and finds the mimimum number of steps between the origin and an intersection
    :param wires: a list of lists of wires
    :return: the minimum number of steps to a cross
    """
    wire_0_pos = get_positions(wires[0])
    wire_1_pos = get_positions(wires[1])

    # find intersections
    intersections = list(set(wire_0_pos).intersection(set(wire_1_pos)))
    intersections.remove((0, 0))
    steps = [wire_0_pos.index(intersection) + wire_1_pos.index(intersection) for intersection in intersections]

    return min(steps)


if __name__ == "__main__":
    wires = read_wires("/Users/rhiannonsteele/PycharmProjects/advent-of-code/day_3/input.txt")
    print(distance(wires))
    print(steps(wires))


