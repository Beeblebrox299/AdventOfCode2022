program_file = "data/10_program.txt"
cycle = 0
X = 1

def one_cycle() -> int:
    globals()['cycle'] += 1
    if (cycle + 20) % 40 == 0:
        return cycle * X
    else:
        return 0


def execute_line(line: list) -> int:
    if line[0] == 'noop':
        return one_cycle()
    elif line[0] == 'addx':
        signal_strength = 0
        signal_strength += one_cycle()
        signal_strength += one_cycle()
        globals()['X'] += int(line[1])
        return signal_strength
    else:
        return 0


def run_program(filename: str) -> int:
    total_signal_strengths = 0
    with open(filename) as program:
        for line in program:
            split_line = line.replace('\n', '').split(' ')
            total_signal_strengths += execute_line(split_line)
    return total_signal_strengths


print(run_program(program_file))
