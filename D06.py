buffer_file = "data/06_datastream_buffer.txt"

def find_marker(buffer_string, marker_type):
    buffer_list = []
    i = 0
    while i < (marker_type - 1):
        buffer_list.append(buffer_string[i])
        i += 1
    while i < len(buffer_string):
        buffer_list.append(buffer_string[i])
        if len(set(buffer_list)) == marker_type:
            return i + 1
        buffer_list.pop(0)
        i += 1


with open(buffer_file) as buffer:
    print(find_marker(buffer.readlines()[0], 14))
