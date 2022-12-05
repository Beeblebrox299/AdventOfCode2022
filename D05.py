crates_file = "data/05_crates.txt"
instructions_file = "data/05_instructions.txt"


def get_uppercase_alphabet():
    alphabet = ''
    for i in range(65, 91):
        alphabet += chr(i)
    return alphabet


def get_nr_of_stacks(filename):
    with open(filename) as stacks:
        last_line = stacks.readlines()[-1]
        nr_of_stacks = len(last_line.split('  '))
        return nr_of_stacks


def convert_stacks_to_lists(filename):
    uppercase_alphabet = get_uppercase_alphabet()
    nr_of_stacks = get_nr_of_stacks(filename)
    list_of_stacks = []
    for i in range(0, nr_of_stacks):
        list_of_stacks.append([])
    with open(filename) as stacks:
        for line in stacks:
            i = 0
            while i < nr_of_stacks:
                letter = line[i*4+1]
                if letter in uppercase_alphabet:
                    list_of_stacks[i].insert(0, letter)
                i += 1
    return list_of_stacks


def parse_instruction_line(line):
    split_line = line.split(' ')
    nr_of_crates = int(split_line[1])
    a = int(split_line[3]) - 1
    b = int(split_line[5]) - 1
    return nr_of_crates, a, b

def carry_out_instruction(line, crate_stacks, crane):
    nr, a, b = parse_instruction_line(line)
    if crane == 9000:
        for i in range(0, nr):
            crate_stacks[b].append(crate_stacks[a].pop())
    elif crane == 9001:
        for i in reversed(range(0, nr)):
            crate_stacks[b].append(crate_stacks[a].pop(-(i+1)))
    return crate_stacks


def move_all_crates(crane):
    crate_stacks = convert_stacks_to_lists(crates_file)
    with open(instructions_file) as instructions:
        for line in instructions:
            crate_stacks = carry_out_instruction(line, crate_stacks, crane)
    return crate_stacks


print(move_all_crates(9001))
