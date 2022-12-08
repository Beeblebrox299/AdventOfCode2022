from D08 import build_tree_list, build_column

trees_file = "data/08_trees.txt"


def get_score_for_one_axis(axis: list, tree_index: int) -> int:
    tree_height = axis[tree_index]
    i = tree_index + 1
    score_forward = 0
    while i < len(axis):
        score_forward += 1
        if axis[i] >= tree_height:
            break
        i += 1
    i = tree_index - 1
    score_backward = 0
    while i >= 0:
        score_backward += 1
        if axis[i] >= tree_height:
            break
        i -= 1
    return score_forward * score_backward


def get_score(forest: list, row: int, tree: int) -> int:
    row_score = get_score_for_one_axis(forest[row], tree)
    column = build_column(forest, tree)
    column_score = get_score_for_one_axis(column, row)
    return row_score * column_score


def find_best_score(filename: str) -> int:
    forest = build_tree_list(filename)
    best_score = 0
    nr_of_rows = len(forest)
    trees_per_row = len(forest[0])
    for row_nr in range(0, nr_of_rows):
        for tree_nr in range(0, trees_per_row):
            score = get_score(forest, row_nr, tree_nr)
            if score > best_score:
                best_score = score
    return best_score


print(find_best_score(trees_file))
