import numpy as np
monkey_file = "data/11_monkeys.txt"

def build_monkey_list(filename: str) -> list:
    monkey_list = [[]]
    current_monkey = 0
    with open(filename) as monkeys:
        for line in monkeys:
            line = line.replace("\n", "").replace(" ", "")
            split_line = line.split(":")
            if len(split_line) == 1:
                current_monkey += 1
                monkey_list.append([])
            elif split_line[0] == "Startingitems":
                monkey_list[current_monkey].append([[int(x)] for x in split_line[1].split(",")])
            elif split_line[0] == "Operation":
                monkey_list[current_monkey].append((split_line[1].replace("new=", "")))
            elif split_line[0] == "Test":
                monkey_list[current_monkey].append(int(split_line[1].replace("divisibleby", "")))
            elif split_line[1]:
                monkey_list[current_monkey].append(int(split_line[1].replace("throwtomonkey", "")))
    for i in range(0, len(monkey_list)):
        monkey_list[i].append(0)
    return monkey_list


def factorisation(n: int) -> list:
    fact = []
    i = 2
    while i <= np.sqrt(np.product(n)):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    fact.append(n)
    return fact


def one_turn(monkey_list: list, monkey_nr: int, reduce_worry_levels: bool) -> list:
    monkey = monkey_list[monkey_nr]
    while monkey[0]:
        old = np.product(monkey[0][0])
        print("old value", monkey[0][0], old)
        new = eval(monkey[1])
        if reduce_worry_levels:
            new //= 3
        new_factorials = factorisation(new)
        if (new % monkey[2]) == 0:
            monkey_list[monkey[3]][0].append(new_factorials)
            print("value", new, "from", monkey_nr, "to", monkey[3], "factorials:", new_factorials)
        else:
            monkey_list[monkey[4]][0].append(new_factorials)
            print("value", new, "from", monkey_nr, "to", monkey[4], "factorials:", new_factorials)
        monkey_list[monkey_nr][5] += 1
        monkey_list[monkey_nr][0].pop(0)
    return monkey_list


def one_round(monkey_list: list, reduce_worry_levels: bool) -> list:
    for i in range(0, len(monkey_list)):
        monkey_list = one_turn(monkey_list, i, reduce_worry_levels)
    return monkey_list


def monkey_in_the_middle(filename: str, rounds: int, reduce_worry_levels: bool) -> int:
    monkey_list = build_monkey_list(filename)
    for i in range(0, rounds):
        print("round", i+1)
        monkey_list = one_round(monkey_list, reduce_worry_levels)
    inspections = []
    for monkey in monkey_list:
        inspections.append(monkey[5])
    print(inspections)
    print(monkey_list)
    inspections = sorted(inspections, reverse=True)
    return inspections[0] * inspections[1]


print(monkey_in_the_middle(monkey_file, 20, True))
