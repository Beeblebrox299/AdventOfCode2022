trees_file = 'data/08_trees.txt'

def build_tree_list(filename: str) -> list:
    tree_list = []
    with open(filename) as trees:
        for line in trees:
            row = []
            line = line.replace('\n', '')
            for tree in line:
                row.append(int(tree))
            tree_list.append(row)
    return tree_list


def check_row(row: list, row_nr: int, is_row: bool = True, is_reversed: bool = False) -> set:
    max_height = -1
    visible_trees = set()
    if is_reversed:
        i = len(row) - 1
        next_tree = -1
    else:
        i = 0
        next_tree = 1
    for tree in row:
        if tree > max_height:
            if is_row:
                visible_trees.add('r'+str(row_nr)+'t'+str(i))
            else:
                visible_trees.add('r'+str(i)+'t'+str(row_nr))
            max_height = tree
        i += next_tree
    if not is_reversed:
        visible_trees.update(check_row(list(reversed(row)), row_nr, is_row, True))
    return visible_trees


def build_column(trees: list, column_nr: int) -> list:
    column = []
    for row in trees:
        column.append(row[column_nr])
    return column


def check_column(trees: list, column_nr: int) -> set:
    column = build_column(trees, column_nr)
    visible_trees = check_row(column, column_nr, False)
    return visible_trees


def count_visible_trees(filename: str) -> int:
    forest = build_tree_list(filename)
    visible_trees = set()
    i = 0
    for row in forest:
        visible_trees.update(check_row(row, i))
        i += 1
    column = 0
    while column < len(forest):
        visible_trees.update(check_column(forest, column))
        column += 1
    return len(visible_trees)


print(count_visible_trees(trees_file))
