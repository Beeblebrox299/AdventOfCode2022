from ast import literal_eval
packet_file = "data/13_packets.txt"

def check_pair(left, right):
    comparisons = min(len(left), len(right))
    for i in range(0, comparisons):
        l_item = left[i]
        r_item = right[i]
        if (type(l_item) == int) & (type(r_item) == int):
            if l_item < r_item:
                return True
            elif l_item > r_item:
                return False
        else:
            if type(l_item) == int:
                l_item = [l_item]
            elif type(r_item) == int:
                r_item = [r_item]
            correct_order = check_pair(l_item, r_item)
            if correct_order is not None:
                return correct_order
    if len(left) < len(right):
        return True
    elif len(right) < len(left):
        return False
    return None


def count_correctly_ordered(filename: str) -> int:
    count = 0
    left = None
    with open(filename) as packets:
        pair_nr = 0
        for line in packets:
            line = line.replace("\n", "")
            if not line:
                left = None
            elif type(left) is not list:
                left = literal_eval(line)
            else:
                pair_nr += 1
                correct_order = check_pair(left, literal_eval(line))
                if correct_order:
                    count += pair_nr
                elif correct_order is None:
                    count += pair_nr
    return count


def get_decoder_key(filename: str) -> int:
    packet_list = []
    with open(filename) as packets:
        for line in packets:
            line = line.replace("\n", "")
            if line:
                packet_list.append(literal_eval(line))
    divider_1 = 1  # indices start at 1
    divider_2 = 2  # divider_1 comes before divider_2
    for packet in packet_list:
        if check_pair(packet, [[2]]):
            divider_1 += 1
            divider_2 += 1
        elif check_pair(packet, [[6]]):
            divider_2 += 1
    return divider_1 * divider_2


print(get_decoder_key(packet_file))
