program_file = "data/10_program.txt"
cycle = 0
X = 1
current_line = 0

def one_cycle(screen: list) -> list:
    global cycle, current_line
    if cycle in range(X-1, X+2):
        screen[current_line] += "#"
    else:
        screen[current_line] += "."
    cycle += 1
    if cycle == 40:
        screen[current_line] += "\n"
        current_line += 1
        cycle = 0
    return screen


def execute_line(line: list, screen: list) -> list:
    global X
    if line[0] == 'noop':
        screen = one_cycle(screen)
    elif line[0] == 'addx':
        screen = one_cycle(screen)
        screen = one_cycle(screen)
        X += int(line[1])
    return screen


def run_program(filename: str) -> str:
    crt_screen_list = []
    for i in range(0, 6):
        crt_screen_list.append("")
    with open(filename) as program:
        for line in program:
            split_line = line.replace('\n', '').split(' ')
            execute_line(split_line, crt_screen_list)
    crt_screen = ""
    for i in range(0, 6):
        crt_screen += crt_screen_list[i]
    return crt_screen


print(run_program(program_file))
