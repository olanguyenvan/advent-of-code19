import sys


def get_fuel_needed(initial_number):
    return initial_number // 3 - 2

def solve_puzzle_1(lines_with_numbers):
    sum_fuel_needed =  sum(map(get_fuel_needed, lines_with_numbers))

    print("Answer for day1, exercise 1: %s" % sum_fuel_needed)


def get_fuel_needed_2(initial_number):
    fuel_needed =  initial_number // 3 - 2

    if fuel_needed >= 0:
        return fuel_needed + get_fuel_needed_2(fuel_needed)
    return 0


def solve_puzzle_2(lines_with_numbers):
    sum_fuel_needed =  sum(map(get_fuel_needed_2, lines_with_numbers))

    print("Answer for day1, exercise 2: %s" % sum_fuel_needed)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No input given. Specify a path to the input file.")
        print("python main.py path-to-input")
    else:
        puzzle_input = open(sys.argv[1]).read()
        lines_with_numbers_str = list(filter(lambda line: line != "", puzzle_input.split("\n")))
        lines_with_numbers_int = list(map(int, lines_with_numbers_str))

        solve_puzzle_1(lines_with_numbers_int)
        solve_puzzle_2(lines_with_numbers_int)
