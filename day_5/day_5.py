class Computer:
    def __init__(self, program):
        self.program = program
        self._instruction_pointer = 0
        self._opcode = None
        self._parameter_modes = None

    @property
    def opcode(self):
        if self._opcode is None:
            self._process_opcode(self.program[self._instruction_pointer])
            return self._opcode
        else:
            return self._opcode

    @property
    def parameter_modes(self):
        if self._parameter_modes is None:
            self._process_opcode(self._opcode)
            return self._parameter_modes
        else:
            return self._parameter_modes

    def _num_params(self):
        if self._opcode == 1:
            num_params = 3
        elif self._opcode == 2:
            num_params = 3
        elif self._opcode == 3:
            num_params = 1
        elif self._opcode == 4:
            num_params = 1
        elif self._opcode == 5:
            num_params = 2
        elif self._opcode == 6:
            num_params = 2
        elif self._opcode == 7:
            num_params = 3
        elif self._opcode == 8:
            num_params = 3
        elif self._opcode == 99:
            num_params = 0
        else:
            raise ValueError("opcode not recognised")

        return num_params

    def _get_parameter(self, index):
        mode = self.parameter_modes[index-1]
        if mode == 0:  # position mode
            out = self.program[self.program[self._instruction_pointer + index]]
        elif mode == 1:  # immediate mode
            out = self.program[self._instruction_pointer + index]
        else:
            raise ValueError("mode not recognised")

        return out

    def add(self):
        parameter_1 = self._get_parameter(1)
        parameter_2 = self._get_parameter(2)
        # clearly the third parameter must be in position mode
        parameter_3 = self.program[self._instruction_pointer + 3]

        self.program[parameter_3] = parameter_1 + parameter_2
        self._instruction_pointer += self._num_params() + 1
        self._opcode = None
        self._parameter_modes = None

    def multiply(self):
        parameter_1 = self._get_parameter(1)
        parameter_2 = self._get_parameter(2)
        # clearly the third parameter must be in position mode
        parameter_3 = self.program[self._instruction_pointer + 3]

        self.program[parameter_3] = parameter_1 * parameter_2
        self._instruction_pointer += self._num_params() + 1
        self._opcode = None
        self._parameter_modes = None

    def take_input(self):
        value = input("Please enter a single integer:\n")
        value = int(value)
        parameter_1 = self.program[self._instruction_pointer + 1]

        self.program[parameter_1] = value
        self._instruction_pointer += self._num_params() + 1
        self._opcode = None
        self._parameter_modes = None

    def output(self):
        value = self._get_parameter(1)
        print(value)
        self._instruction_pointer += self._num_params() + 1
        self._opcode = None
        self._parameter_modes = None

    def jump_if_true(self):
        parameter_1 = self._get_parameter(1)
        parameter_2 = self._get_parameter(2)

        if parameter_1 != 0:
            self._instruction_pointer = parameter_2
        else:
            self._instruction_pointer += self._num_params() + 1

        self._opcode = None
        self._parameter_modes = None

    def jump_if_false(self):
        parameter_1 = self._get_parameter(1)
        parameter_2 = self._get_parameter(2)

        if parameter_1 == 0:
            self._instruction_pointer = parameter_2
        else:
            self._instruction_pointer += self._num_params() + 1

        self._opcode = None
        self._parameter_modes = None

    def less_than(self):
        parameter_1 = self._get_parameter(1)
        parameter_2 = self._get_parameter(2)
        parameter_3 = self.program[self._instruction_pointer + 3]

        if parameter_1 < parameter_2:
            self.program[parameter_3] = 1
        else:
            self.program[parameter_3] = 0

        self._instruction_pointer += self._num_params() + 1
        self._opcode = None
        self._parameter_modes = None

    def equals(self):
        parameter_1 = self._get_parameter(1)
        parameter_2 = self._get_parameter(2)
        parameter_3 = self.program[self._instruction_pointer + 3]

        if parameter_1 == parameter_2:
            self.program[parameter_3] = 1
        else:
            self.program[parameter_3] = 0

        self._instruction_pointer += self._num_params() + 1
        self._opcode = None
        self._parameter_modes = None

    def _process_opcode(self, in_opcode):
        """
        Processes an opcode, eg. 1002
        ABCDE
         1002

        DE - two-digit opcode,      02 == opcode 2
         C - mode of 1st parameter,  0 == position mode
         B - mode of 2nd parameter,  1 == immediate mode
         A - mode of 3rd parameter,  0 == position mode,
                                          omitted due to being a leading zero

        :return: the opcode and the parameter modes in order.
        """
        whole_opcode = in_opcode
        opcode = int(str(whole_opcode)[-2:])
        self._opcode = opcode

        param_modes = str(whole_opcode)[:-2]
        param_modes = param_modes[::-1]
        processed_param_modes = [0] * self._num_params()
        for i in range(0, len(param_modes)):
            processed_param_modes[i] = int(param_modes[i])

        self._parameter_modes = processed_param_modes

    def run(self):
        """
        Runs the program
        updates program
        """

        while self.opcode != 99:
            if self.opcode == 1:
                self.add()
            elif self.opcode == 2:
                self.multiply()
            elif self.opcode == 3:
                self.take_input()
            elif self.opcode == 4:
                self.output()
            elif self.opcode == 5:
                self.jump_if_true()
            elif self.opcode == 6:
                self.jump_if_false()
            elif self.opcode == 7:
                self.less_than()
            elif self.opcode == 8:
                self.equals()
            else:
                raise ValueError("Opcode not recognised")

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
    c = Computer.load("/Users/rhiannonsteele/PycharmProjects/advent-of-code/day_5/input.txt")
    c.run()


