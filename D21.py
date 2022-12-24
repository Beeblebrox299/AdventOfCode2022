import operator
from tqdm import tqdm
monkey_file = "data/21_monkeys.txt"

def build_monkey_dict(filename: str) -> dict:
    monkeys = {}
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split(": ")
            try:
                monkeys[line[0]] = int(line[1])
            except ValueError:
                monkeys[line[0]] = line[1].split(" ")
    return monkeys


def find_monkey_value(filename: str, my_monkey: str, monkey_dict: dict = None):
    if not monkey_dict:
        monkey_dict = build_monkey_dict(filename)
    while type(monkey_dict[my_monkey]) == list:
        for monkey in monkey_dict:
            if type(monkey_dict[monkey]) == list:
                operation = monkey_dict[monkey]
                if (type(monkey_dict[operation[0]]) == int) & (type(monkey_dict[operation[2]]) == int):
                    monkey_dict[monkey] = int(eval("monkey_dict['" + operation[0] + "'] " + operation[1] +
                                                   " monkey_dict['" + operation[2] + "']"))
    return monkey_dict[my_monkey]


def perform_operation(monkey_dict: dict, monkey: str, first_monkey: str, second_monkey: str) -> None:
    operator_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
    if (type(monkey_dict[first_monkey]) == int) & (type(monkey_dict[second_monkey]) == int):
        monkey_dict[monkey] = operator_dict[monkey_dict[monkey][1]](monkey_dict[first_monkey],
                                                                    monkey_dict[second_monkey])


def equation_step(monkey_dict: dict, monkey: str):
    if type(monkey_dict[monkey]) == list:
        first_monkey = monkey_dict[monkey][0]
        second_monkey = monkey_dict[monkey][2]
        if (type(monkey_dict[first_monkey]) == int) & (type(monkey_dict[second_monkey]) == int):
            perform_operation(monkey_dict, monkey, first_monkey, second_monkey)
        else:
            if type(first_monkey) == str:
                equation_step(monkey_dict, first_monkey)
                monkey_dict[monkey][0] = monkey_dict[first_monkey]
            if type(second_monkey) == str:
                equation_step(monkey_dict, second_monkey)
                monkey_dict[monkey][2] = monkey_dict[second_monkey]
            perform_operation(monkey_dict, monkey, first_monkey, second_monkey)
    return monkey_dict


def solve_equation(equation: list, i: int) -> int:
    operator_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
    equation_copy = [x for x in equation]
    for j in [0, 2]:
        if type(equation_copy[j]) == list:
            equation_copy[j] = solve_equation(equation_copy[j], i)
        elif equation_copy[j] is None:
            equation_copy[j] = i
    solution = operator_dict[equation_copy[1]](equation_copy[0], equation_copy[2])
    return solution


def get_humn_number(filename: str) -> int:
    # I just don't care about a good, arithmetical solution at this point
    monkey_dict = build_monkey_dict(filename)
    monkey_dict["humn"] = None
    monkey_dict["root"][1] = "=="
    equation_step(monkey_dict, "root")
    my_equation = monkey_dict["root"][0]
    solution = -1
    i = 3378273070690
    while solution != monkey_dict["root"][2]:
        i += 1
        solution = solve_equation(my_equation, i)
        print(i, solution, monkey_dict["root"][2])
    return i


print(get_humn_number(monkey_file))
