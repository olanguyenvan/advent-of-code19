import sys
from datetime import datetime


def solve_puzzle_1(numbers_int, noun = 12, verb = 2):
    numbers_int[1] = noun
    numbers_int[2] = verb

    def run_the_program(index = 0):
        opcode = numbers_int[index]

        def add_operation():
            numbers_int[numbers_int[index + 3]] = numbers_int[numbers_int[index + 1]] + numbers_int[numbers_int[index + 2]]
            run_the_program(index + 4)


        def mult_operation():
            numbers_int[numbers_int[index + 3]] = numbers_int[numbers_int[index + 1]] *  numbers_int[numbers_int[index + 2]]
            run_the_program(index + 4)

        def halt_program():
            pass

        switcher = {
            1: add_operation,
            2: mult_operation,
            99: halt_program,
        }

        switcher[opcode]()

    run_the_program()

    return numbers_int[0]


def solve_puzzle_2(numbers_int):
    expected_output = 19690720
   
    for noun in range(99):
        for verb in range(99):
            numbers_int_copy = numbers_int[:]

            solve_puzzle_1(numbers_int_copy, noun, verb)

            if numbers_int_copy[0] == expected_output:
                print(noun, verb)
                return 100 * noun + verb


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No input given. Specify a path to the input file.")
        print("python main.py path-to-input")
    else:
        puzzle_input = open(sys.argv[1]).read()
        numbers_str = list(filter(lambda line: line != "", puzzle_input.split(",")))
        numbers_int = list(map(int, numbers_str))

        start_ex_1 = datetime.now()
        solution_1 = solve_puzzle_1(numbers_int[:])
        print("Answer for day1, exercise 1: %s" % solution_1)
        print(datetime.now() - start_ex_1)


        start_ex_2 = datetime.now()
        solution_2 = solve_puzzle_2(numbers_int[:])
        print("Answer for day1, exercise 2: %s" % solution_2)
        print(datetime.now() - start_ex_2)
