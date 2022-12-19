from tqdm import tqdm
map_file = "data/12_elevation_map.txt"

def parse_file(filename: str) -> list:
    map_list = []
    with open(filename) as file:
        for line in file:
            current_line = []
            line = line.replace("\n", "")
            for char in line:
                current_line.append(char)
            map_list.append(current_line)
    return map_list


def get_height_value(height: str) -> int:
    if height == "S":
        value = 97
    elif height == "E":
        value = 122
    else:
        value = ord(height)
    return value


def can_reach(x_0: int, y_0: int, x_1: int, y_1: int, map_list: list):
    try:
        current_val = get_height_value(map_list[y_0][x_0])
        next_val = get_height_value(map_list[y_1][x_1])
    except IndexError:
        return False
    if (current_val - next_val) <= 1:
        return str(y_1) + "_" + str(x_1)
    return False


def check_for_edges(x: int, y: int, map_list: list) -> list:
    edges = []
    edge_1 = can_reach(x, y, x + 1, y, map_list)
    edge_2 = can_reach(x, y, x, y + 1, map_list)
    if x - 1 >= 0:
        edge_3 = can_reach(x, y, x - 1, y, map_list)
    else:
        edge_3 = False
    if y - 1 >= 0:
        edge_4 = can_reach(x, y, x, y - 1, map_list)
    else:
        edge_4 = False
    for i in range(1, 5):
        edge = eval("edge_" + str(i))
        if edge:
            edges.append(edge)
    return edges


def build_graph(filename: str) -> (str, str, dict, list):
    map_list = parse_file(filename)
    graph = {}
    possible_starts = []
    for i in range(0, len(map_list)):
        for j in range(0, len(map_list[i])):
            graph[str(i) + "_" + str(j)] = {"edges": check_for_edges(j, i, map_list)}
            if map_list[i][j] == "a":
                possible_starts.append(str(i) + "_" + str(j))
            elif map_list[i][j] == "S":
                start = str(i) + "_" + str(j)
                possible_starts.append(str(i) + "_" + str(j))
            elif map_list[i][j] == "E":
                end = str(i) + "_" + str(j)
    return start, end, graph, possible_starts


def bellman_ford(start: str, graph: dict) -> dict:
    max_path = len(graph)
    for point in graph:
        graph[point]["distance"] = max_path
        graph[point]["p"] = None
    graph[start]["distance"] = 0
    for i in tqdm(range(0, int(len(graph) * 1.5)), desc="Finding distances"):
        for point in graph:
            for edge in graph[point]["edges"]:
                if graph[edge]["distance"] > graph[point]["distance"] + 1:
                    graph[edge]["distance"] -= 1
                    graph[edge]["p"] = point
    return graph


def find_shortest_path(filename: str, part_2: bool) -> int:
    start, end, graph, possible_starts = build_graph(filename)
    graph_with_distances = bellman_ford(end, graph)
    if part_2:
        shortest_path = len(graph)
        for point in tqdm(possible_starts, desc="Checking all possible startpoints"):
            distance = graph_with_distances[point]["distance"]
            if distance < shortest_path:
                shortest_path = distance
    else:
        shortest_path = graph_with_distances[start]["distance"]
    return shortest_path


print(find_shortest_path(map_file, True))
