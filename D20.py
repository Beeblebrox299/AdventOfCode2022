from tqdm import tqdm
coordinates_file = "data/20_coordinates.txt"

def mix_once(coordinates: list, order: list) -> list:
    length = len(coordinates)
    for i in range(0, length):
        item = order[i]
        value = item[0]
        current_position = coordinates.index(item)
        new_position = (current_position + value) % (length - 1)
        coordinates.pop(current_position)
        coordinates.insert(new_position, item)
    return coordinates


def get_grove_coordinates(filename: str, part_2: bool) -> int:
    coordinates = []
    with open(filename) as file:
        for line in file:
            if part_2:
                coordinates.append([int(line) * 811589153, len(coordinates)])
            else:
                coordinates.append([int(line), len(coordinates)])
    if part_2:
        mix_n_times = 10
    else:
        mix_n_times = 1
    mixed_coordinates = coordinates[:]
    for i in tqdm(range(0, mix_n_times)):
        mixed_coordinates = mix_once(mixed_coordinates, coordinates)
    for i in range(0, len(mixed_coordinates)):
        mixed_coordinates[i] = mixed_coordinates[i][0]
    grove_coordinates = 0
    for i in range(1, 4):
        grove_coordinates += mixed_coordinates[(i * 1000 + mixed_coordinates.index(0)) % len(mixed_coordinates)]
    return grove_coordinates


print(get_grove_coordinates(coordinates_file, True))
