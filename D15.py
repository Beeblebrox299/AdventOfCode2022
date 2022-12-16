import numpy as np
sensor_file = "data/15_sensors.txt"

def get_distance(a: list, b: list) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_sensor_range(cave_line, sensor: list, beacon: list, row: int, min_x: int, max_x: int) -> list:
    beacon_distance = get_distance(sensor, beacon)
    if sensor[1] == row:
        cave_line[sensor[0]] = "S"
    if beacon[1] == row:
        cave_line[beacon[0]] = "B"
    for i in range(min_x, max_x):
        if cave_line[i] == ".":
            if get_distance(sensor, [i, row]) <= beacon_distance:
                cave_line[i] = "#"
    return cave_line


def get_sensor_data(filename: str) -> (list, list, list):
    sensors = []
    beacons = []
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    with open(filename) as file:
        for line in file:
            split_line = line.split(":")
            sensor = split_line[0].replace("Sensor at x=", "")
            sensor = [int(i) for i in sensor.split(", y=")]
            beacon = split_line[1].replace(" closest beacon is at x=", "")
            beacon = [int(i) for i in beacon.split(", y=")]
            min_x = min(min_x, sensor[0], beacon[0])
            max_x = max(max_x, sensor[0], beacon[0])
            min_y = min(min_y, sensor[1], beacon[1])
            max_y = max(max_y, sensor[1], beacon[1])
            sensors.append(sensor)
            beacons.append(beacon)
    return sensors, beacons, [min_x, max_x, min_y, max_y]


def count_string_locations(filename: str, row_number: int, search_for: str, max_length: int = 0) -> (int, list):
    sensors, beacons, min_max = get_sensor_data(filename)
    if max_length:
        min_x = 0
        max_x = max_length
    else:
        min_x = min_max[0] - (min_max[3] - min_max[2])
        max_x = min_max[1] + (min_max[3] - min_max[2])
    cave_line = np.full((max_x - min_x), ".")
    for i in range(0, len(sensors)):
        get_sensor_range(cave_line, sensors[i], beacons[i], row_number, min_x, max_x)
        print("mapped sensor", i + 1, "of", len(sensors), "on line", row_number)
    found_items = np.where(cave_line == search_for)
    positions = list(found_items[0])
    count = len(positions)
    return count, positions


def get_tuning_frequency(filename: str, max_location) -> int:
    for i in range(0, max_location + 1):
        free_space, position = count_string_locations(filename, i, ".", max_location + 1)
        print(free_space, position)
        if free_space:
            return position[0] * 4000000 + i


print(get_tuning_frequency(sensor_file, 4000000))
