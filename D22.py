map_file = "data/22_boardmap.txt"

def build_boardlist(filename) -> (list, str):
    boardlist = []
    is_path = False
    max_len = 0
    path = ''
    with open(filename) as file:
        for line in file:
            if (line != "\n") & (not is_path):
                line = [x for x in line.replace("\n", "")]
                boardlist.append(line)
                if len(line) > max_len:
                    max_len = len(line)
            elif line == "\n":
                is_path = True
            elif is_path:
                path += line.replace("\n", "")
    for item in boardlist:
        while len(item) < max_len:
            item.append(" ")
    return boardlist, path


def one_step(boardlist: list, position: list, dimension: str, direction: int) -> (list, bool):
    if dimension == "x":
        length = len(boardlist[position[1]])
        next_field = boardlist[position[1]][(position[0] + direction) % length]
        if next_field == ".":
            position[0] = (position[0] + direction) % length
            return position, True
        elif next_field == " ":
            new_position = [(position[0] + direction) % length, position[1]]
            new_position, moved = one_step(boardlist, new_position, dimension, direction)
            if moved:
                return new_position, True
            else:
                return position, False
        elif next_field == "#":
            return position, False
    elif dimension == "y":
        length = len(boardlist)
        next_field = boardlist[(position[1] + direction) % length][position[0]]
        if next_field == ".":
            position[1] = (position[1] + direction) % length
            return position, True
        elif next_field == " ":
            new_position = [position[0], (position[1] + direction) % length]
            new_position, moved = one_step(boardlist, new_position, dimension, direction)
            if moved:
                return new_position, True
            else:
                return position, False
        elif next_field == "#":
            return position, False


def move(boardlist: list, position: list, facing: int, steps: int) -> list:
    if facing == 0:
        dimension, direction = "x", 1
    elif facing == 1:
        dimension, direction = "y", 1
    elif facing == 2:
        dimension, direction = "x", -1
    elif facing == 3:
        dimension, direction = "y", -1
    for i in range(0, steps):
        position, moved = one_step(boardlist, position, dimension, direction)
        if not moved:
            return position
    return position


def walk_path(boardlist: list, path: str, starting_position: tuple = (0, 0, 0)) -> (list, str):
    facing = starting_position[2]
    position = [starting_position[0], starting_position[1]]
    steps = '0'
    while boardlist[position[1]][position[0]] != ".":
        position[0] += 1
    for char in path:
        if char.isdigit():
            steps += char
        else:
            position = move(boardlist, position, facing, int(steps))
            steps = '0'
            if char == "R":
                facing = (facing + 1) % 4
            elif char == "L":
                facing = (facing - 1) % 4
    position = move(boardlist, position, facing, int(steps))
    final_position = [(position[0] + 1) % len(boardlist[position[1]]), (position[1] + 1) % len(boardlist)]
    return final_position, facing


def get_passwd(filename) -> int:
    boardlist, path = build_boardlist(filename)
    end_position, facing = walk_path(boardlist, path)
    passwd = 1000 * end_position[1] + 4 * end_position[0] + facing
    return passwd


print(get_passwd(map_file))
