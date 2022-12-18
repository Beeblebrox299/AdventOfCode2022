cubes_file = "data/18_cubes.txt"

def sort_by_z(cube: list) -> int:
    return cube[2]


def count_free_sides(filename) -> int:
    cubes = []
    with open(filename) as file:
        for line in file:
            cubes.append([int(x) for x in line.split(",")])
    cubes = sorted(cubes)
    free_sides = len(cubes) * 6
    for cube in cubes:
        same_x = [x for x in cubes if x[0] == cube[0]]
        same_x.remove(cube)
        for second_cube in same_x:
            if (cube[1] == second_cube[1]) & (abs(cube[2] - second_cube[2]) == 1) | (cube[2] == second_cube[2]) & (abs(cube[1] - second_cube[1]) == 1):
                free_sides -= 1
    cubes = sorted(cubes, key=sort_by_z)
    for cube in cubes:
        same_z = [x for x in cubes if x[2] == cube[2]]
        same_z.remove(cube)
        for second_cube in same_z:
            if (cube[1] == second_cube[1]) & (abs(cube[0] - second_cube[0]) == 1):
                free_sides -= 1
    return free_sides


print(count_free_sides(cubes_file))
