import numpy as np


def part1():
    with open("input.txt") as file:
        rows_first = [[int(letter) for letter in line] for line in file.read().split("\n")]
    visible_trees = 0
    columns_first = np.transpose(rows_first).tolist()
    size = len(rows_first)
    for i in range(1, size-1):
        for j in range(1, size-1):
            a = rows_first[i][j]
            if a > max(rows_first[i][:j]) or a > max(rows_first[i][j+1:]) or a > max(columns_first[j][:i]) or a > max(columns_first[j][i+1:]):
                visible_trees += 1
    return visible_trees + 4*size - 4


print(part1())
