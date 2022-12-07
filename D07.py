logfile = "data/07_terminal_logs.txt"
current_dir_tree = []
filesystem = []
dir_list = []
total_space = 70000000
needed_space = 30000000

def parse_line(line):
    log_as_list = line.split(" ")
    if log_as_list[0] == '$':
        handle_command(log_as_list[1:])
    elif log_as_list[0] != 'dir':
        add_file(log_as_list[0])


def handle_command(command):
    if command[0] == 'cd':
        if command[1] == '..':
            current_dir_tree.pop()
        else:
            current_dir_tree.append(command[1])
            add_dir(''.join(current_dir_tree))


def add_dir(name):
    globals()[name] = []
    dir_list.append(name)
    if not filesystem:
        filesystem.append(globals()[name])
    else:
        globals()[''.join(current_dir_tree[:-1])].append(globals()[name])


def add_file(size):
    globals()[''.join(current_dir_tree)].append(int(size))


def build_filesystem():
    with open(logfile) as logs:
        for log_line in logs:
            log_line = log_line.replace("\n", "")
            parse_line(log_line)


def flatten_list(multi_d_list, flat_list=None):
    if flat_list is None:
        flat_list = []
    i = 0
    for item in multi_d_list:
        i += 1
        if type(item) == list:
            flatten_list(item, flat_list)
        else:
            flat_list.append(item)
    return flat_list


def get_dir_size(directory):
    flattened_dir = flatten_list(globals()[directory])
    return sum(flattened_dir)


def get_sum_of_dirs(max_size):
    build_filesystem()
    total_size = 0
    for directory in dir_list:
        dir_size = get_dir_size(directory)
        if dir_size <= max_size:
            total_size += dir_size
    return total_size


def find_dir_to_delete():
    build_filesystem()
    total_size = get_dir_size('/')
    free_space = total_space - total_size
    chosen_dir_size = total_size
    for directory in dir_list:
        dir_size = get_dir_size(directory)
        if dir_size + free_space >= needed_space:
            if dir_size < chosen_dir_size:
                chosen_dir_size = dir_size
    return chosen_dir_size


print(find_dir_to_delete())
