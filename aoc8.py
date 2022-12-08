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


def part2():
    with open("input.txt") as file:
        tree_map = [[int(letter) for letter in line] for line in file.read().split("\n")]
    max_ss = 1  # max scenic score
    size = len(tree_map)
    for i in range(size):
        for j in range(size):
            cur_ss = 1  # current scenic score
            k = 1
            while i+k+1 < size and tree_map[i+k][j] < tree_map[i][j]:
                k += 1
            cur_ss *= k
            k = 1
            while j+k+1 < size and tree_map[i][j+k] < tree_map[i][j]:
                k += 1
            cur_ss *= k
            k = 1
            while i-k-1 >= 0 and tree_map[i-k][j] < tree_map[i][j]:
                k += 1
            cur_ss *= k
            k = 1
            while j-k-1 >= 0 and tree_map[i][j-k] < tree_map[i][j]:
                k += 1
            cur_ss *= k
            if cur_ss > max_ss:
                max_ss = cur_ss
    return max_ss


print(f"Part 1: {part1()}\nPart 2: {part2()}")
