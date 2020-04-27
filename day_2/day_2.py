class Computer:
    def __init__(self, program):
        self.program = program
        self._instruction_pointer = 0

    def add(self):
        parameter_1 = self.program[self._instruction_pointer + 1]
        parameter_2 = self.program[self._instruction_pointer + 2]
        parameter_3 = self.program[self._instruction_pointer + 3]

        self.program[parameter_3] = self.program[parameter_1] + self.program[parameter_2]
        self._instruction_pointer += 4

    def multiply(self):
        parameter_1 = self.program[self._instruction_pointer + 1]
        parameter_2 = self.program[self._instruction_pointer + 2]
        parameter_3 = self.program[self._instruction_pointer + 3]

        self.program[parameter_3] = self.program[parameter_1] * self.program[parameter_2]
        self._instruction_pointer += 4

    def run(self):
        """
        Runs the program
        updates program
        """
        opcode = self.program[self._instruction_pointer]
        while opcode != 99:
            if opcode == 1:
                self.add()
                opcode = self.program[self._instruction_pointer]
            elif opcode == 2:
                self.multiply()
                opcode = self.program[self._instruction_pointer]

    @staticmethod
    def load(file_path: str):
        """
        loads an intcode program
        :param file_path: The full path to the input file containing the program
        :return: the program to work on as a list of ints
        """

        f = open(file_path, 'r')
        raw = f.read()
        program = raw.split(',')
        program = [int(item) for item in program]

        return Computer(program)


if __name__ == "__main__":

    for noun in range(0, 100):
        for verb in range(0, 100):
            c = Computer.load("/Users/rhiannonsteele/PycharmProjects/advent-of-code/day_2/input.txt")
            c.program[1] = noun
            c.program[2] = verb
            c.run()
            if c.program[0] == 19690720:
                print("noun = {}, verb = {}".format(noun, verb))
                print("100 * noun + verb = {}".format(100 * noun + verb))
                break


