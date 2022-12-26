positions_file = "data/23_elf_positions.txt"

def build_map(filename: str) -> list:
    elf_map = []
    with open(filename) as file:
        for line in file:
            line = [x for x in line.replace("\n", "")]
            elf_map.append(line)
    return elf_map

def is_free(elf_map: list, position: tuple, direction: str) -> (bool, tuple):
    if direction == "N":
        tile1 = elf_map[position[0] - 1][position[1] - 1]
        tile2 = elf_map[position[0] - 1][position[1]]
        tile3 = elf_map[position[0] - 1][position[1] + 1]
        new_position = (position[0] - 1, position[1])
    elif direction == "S":
        tile1 = elf_map[position[0] + 1][position[1] - 1]
        tile2 = elf_map[position[0] + 1][position[1]]
        tile3 = elf_map[position[0] + 1][position[1] + 1]
        new_position = (position[0] + 1, position[1])
    elif direction == "W":
        tile1 = elf_map[position[0] - 1][position[1] - 1]
        tile2 = elf_map[position[0]][position[1] - 1]
        tile3 = elf_map[position[0] + 1][position[1] - 1]
        new_position = (position[0], position[1] - 1)
    else:
        tile1 = elf_map[position[0] - 1][position[1] + 1]
        tile2 = elf_map[position[0]][position[1] + 1]
        tile3 = elf_map[position[0] + 1][position[1] + 1]
        new_position = (position[0], position[1] + 1)
    if tile1 == tile2 == tile3 == ".":
        return True, new_position
    else:
        return False, position


def need_to_move(elf_map: list, position: tuple) -> bool:
    if not is_free(elf_map, position, "N")[0]:
        return True
    if not is_free(elf_map, position, "S")[0]:
        return True
    if not is_free(elf_map, position, "W")[0]:
        return True
    if not is_free(elf_map, position, "E")[0]:
        return True
    return False


def bigger_map(elf_map: list) -> list:
    for item in elf_map:
        item.insert(0, '.')
        item.append('.')
    row_len = len(elf_map[0])
    elf_map.insert(0, ['.' for x in range(0, row_len)])
    elf_map.append(['.' for x in range(0, row_len)])
    return elf_map


def one_round(elf_map: list, round_nr: int) -> (list, bool):
    elf_map = bigger_map(elf_map)
    direction_order = {0: "N", 1: "S", 2: "W", 3: "E"}
    propositions = {}
    moves = []
    for i in range(0, len(elf_map)):
        for j in range(0, len(elf_map[i])):
            if elf_map[i][j] == '#':
                if need_to_move(elf_map, (i, j)):
                    direction = round_nr
                    for k in range(0, 4):
                        free, new_position = is_free(elf_map, (i, j), direction_order[((direction + k) % 4)])
                        if free:
                            propositions[(i, j)] = new_position
                            moves.append(new_position)
                            break
    valid_moves = [x for x in set(moves) if moves.count(x) == 1]
    if not valid_moves:
        return elf_map, False
    for elf in propositions:
        if propositions[elf] in valid_moves:
            new_position = propositions[elf]
            elf_map[elf[0]][elf[1]] = "."
            elf_map[new_position[0]][new_position[1]] = "#"
    return elf_map, True


def find_smallest_rectangle(elf_map: list) -> list:
    while elf_map[0].count('#') == 0:
        elf_map.pop(0)
    while elf_map[-1].count('#') == 0:
        elf_map.pop(-1)
    first_elf = len(elf_map[0])
    last_elf = 0
    for item in elf_map:
        if item.count('#') > 0:
            if item.index('#') < first_elf:
                first_elf = item.index('#')
    for i in range(0, first_elf):
        for item in elf_map:
            item.pop(0)
    for item in elf_map:
        if item.count('#') > 0:
            index = ''.join(item).rindex('#')
            if index > last_elf:
                last_elf = index
    for i in range(0, len(elf_map[0]) - last_elf - 1):
        for item in elf_map:
            item.pop()
    return elf_map


def count_empty_tiles(filename: str) -> int:
    elf_map = build_map(filename)
    for i in range(0, 10):
        elf_map = one_round(elf_map, i)[0]
    elf_map = find_smallest_rectangle(elf_map)
    empty_tiles = 0
    for line in elf_map:
        empty_tiles += line.count('.')
    return empty_tiles


def complete_simulation(filename: str) -> int:
    elf_map = build_map(filename)
    i, moved = 0, True
    while moved:
        elf_map, moved = one_round(elf_map, i)
        elf_map = find_smallest_rectangle(elf_map)
        i += 1
    return i


print("part 1:", count_empty_tiles(positions_file))
print("part 2:", complete_simulation(positions_file))
