rocks_file = "data/14_rocks.txt"
min_x = 439  # searched for manually (440)

def add_rock(start: list, end: list, rock_formation: list) -> list:
    while len(rock_formation) < max(start[1], end[1]) + 1:
        rock_formation.append([])
        for item in rock_formation[0]:
            rock_formation[-1].append(".")
    while len(rock_formation[0]) < max(start[0], end[0]) + 1:
        for line in rock_formation:
            line.append(".")
    if start[0] == end[0]:
        for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            rock_formation[i][start[0]] = "#"
    else:
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            rock_formation[start[1]][i] = "#"
    return rock_formation


def build_rock_formation(filename: str) -> list:
    rock_formation = [[]]
    with open(filename) as rocks:
        for line in rocks:
            line = line.split("->")
            for pair in line:
                split_pair = pair.split(",")
                for i in range(0, len(split_pair)):
                    split_pair[i] = int(split_pair[i])
                split_pair[0] -= min_x
                if line.index(pair) == 0:
                    start = split_pair
                else:
                    rock_formation = add_rock(start, split_pair, rock_formation)
                    start = split_pair
    while len(rock_formation[0]) <= (len(rock_formation) * 2):
        for line in rock_formation:
            line.append(".")
    return rock_formation


def one_grain(rock_formation: list) -> (list, bool):
    grain_position = [500 - min_x, 0]
    while grain_position[1] < len(rock_formation) - 1:
        x, y = grain_position[0], grain_position[1]
        if rock_formation[y + 1][x] == ".":
            grain_position[1] += 1
        elif rock_formation[y + 1][x - 1] == ".":
            grain_position[1] += 1
            grain_position[0] -= 1
        elif rock_formation[y + 1][x + 1] == ".":
            grain_position[1] += 1
            grain_position[0] += 1
        else:
            rock_formation[y][x] = "°"
            return rock_formation, True
    rock_formation[grain_position[1]][grain_position[0]] = "°"
    return rock_formation, False


def simulate_sand_until_void(rock_formation: list, grain_count: int = 0) -> int:
    rock_formation, grain_stopped = one_grain(rock_formation)
    if grain_stopped:
        grain_count = simulate_sand_until_void(rock_formation, grain_count + 1)
    return grain_count


def simulate_sand_until_full(rock_formation: list) -> int:
    rock_formation.append([])
    for item in rock_formation[0]:
        rock_formation[-1].append(".")
    grain_count = 0
    while rock_formation[0][500 - min_x] == ".":
        grain_count += 1
        rock_formation = one_grain(rock_formation)[0]
    for line in rock_formation:
        print(line)
    return grain_count


def count_grains(filename: str) -> int:
    rock_formation = build_rock_formation(filename)
    grain_count = simulate_sand_until_full(rock_formation)
    return grain_count


print(count_grains(rocks_file))
