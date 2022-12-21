from ast import literal_eval
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


def find_root_value(filename: str, monkey_dict: dict = None):
    if not monkey_dict:
        monkey_dict = build_monkey_dict(filename)
    while type(monkey_dict["root"]) == list:
        for monkey in monkey_dict:
            if type(monkey_dict[monkey]) == list:
                operation = monkey_dict[monkey]
                if (type(monkey_dict[operation[0]]) == int) & (type(monkey_dict[operation[2]]) == int):
                    monkey_dict[monkey] = int(eval("monkey_dict['" + operation[0] + "'] " + operation[1] +
                                                   " monkey_dict['" + operation[2] + "']"))
    return monkey_dict["root"]


def get_humn_number(filename: str) -> int:
    # This brute force approach works for the example input. On the real input, I let i go up to ~27k before stopping.
    # So it either doesn't work or the solution is higher than 27k.
    # It already took several minutes to get to 27k, so I should find a better approach.
    monkey_dict = build_monkey_dict(filename)
    monkey_dict["root"][1] = '=='
    i = 0
    monkey_dict["humn"] = i
    monkeys = monkey_dict.copy()
    while not find_root_value("", monkeys):
        i += 1
        monkeys = monkey_dict.copy()
        monkeys["humn"] = i
    return i


print(get_humn_number(monkey_file))
