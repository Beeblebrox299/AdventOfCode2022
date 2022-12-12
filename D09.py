from math import copysign
movements_file = "data/09_movements.txt"
head_position = [0, 0]
tail_position = [0, 0]

def move(axis: int, direction: int, steps: int, rope: list):
    positions_visited_by_tail = set()
    for i in range(0, steps):
        rope[0][axis] += direction
        for j in range(1, len(rope)):
            distance_x = rope[j-1][0] - rope[j][0]
            distance_y = rope[j-1][1] - rope[j][1]
            if (not distance_x) | (not distance_y):
                if distance_x:
                    distance = distance_x
                elif distance_y:
                    distance = distance_y
                else:
                    distance = 0
            else:
                distance = distance_x * distance_y
            if distance not in range(-1, 2):
                same_column = rope[j-1][0] == rope[j][0]
                same_row = rope[j-1][1] == rope[j][1]
                if (not same_column) & (not same_row):
                    tail_direction_x = copysign(1, distance_x)
                    tail_direction_y = copysign(1, distance_y)
                    rope[j][0] += tail_direction_x
                    rope[j][1] += tail_direction_y
                elif not same_column:
                    tail_direction = copysign(1, distance_x)
                    rope[j][0] += tail_direction
                elif not same_row:
                    tail_direction = copysign(1, distance_y)
                    rope[j][1] += tail_direction
            positions_visited_by_tail.add(tuple(rope[-1]))
    return positions_visited_by_tail


def execute_one_instruction(direction: str, steps: int, rope: list):
    if direction == 'L':
        positions_visited_by_tail = move(0, 1, steps, rope)
    elif direction == 'R':
        positions_visited_by_tail = move(0, -1, steps, rope)
    elif direction == 'U':
        positions_visited_by_tail = move(1, 1, steps, rope)
    elif direction == 'D':
        positions_visited_by_tail = move(1, -1, steps, rope)
    else:
        return set()
    return positions_visited_by_tail


def simulate_movements(rope_length: int):
    positions_visited_by_tail = {(0, 0)}
    rope = []
    for i in range(0,rope_length):
        rope.append([0, 0])
    with open(movements_file) as movements:
        for line in movements:
            line.replace('\n', '')
            instructions = line.split(' ')
            positions_visited_by_tail.update(execute_one_instruction(instructions[0], int(instructions[1]), rope))
    return positions_visited_by_tail


print(len(simulate_movements(10)))
