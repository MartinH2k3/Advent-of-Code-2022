def neighbours1(coord, matrix):
    alphabet = 'SabcdefghijklmnopqrstuvwxyzE'
    output = []
    y, x = coord[0], coord[1]
    if y > 0 and alphabet.index(matrix[y-1][x]) - alphabet.index(matrix[y][x]) <= 1:
        output.append([y-1, x])
    if y < len(matrix)-1 and alphabet.index(matrix[y+1][x]) - alphabet.index(matrix[y][x]) <= 1:
        output.append([y+1, x])
    if x > 0 and alphabet.index(matrix[y][x-1]) - alphabet.index(matrix[y][x]) <= 1:
        output.append([y, x-1])
    if x < len(matrix[0])-1 and alphabet.index(matrix[y][x+1]) - alphabet.index(matrix[y][x]) <= 1:
        output.append([y, x+1])
    return output


def part1():
    with open("input.txt") as file:
        matrix = [list(row) for row in file.read().split("\n")]
    for index, row in enumerate(matrix):
        if "S" in row:
            start = [index, row.index("S")]
        if "E" in row:
            end = [index, row.index("E")]
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)
    levels = 1
    cur_level = 1
    next_level = 0
    while len(queue):
        for neighbour in neighbours1(queue.pop(0), matrix):
            if neighbour not in visited:
                if neighbour == end:
                    return levels
                queue.append(neighbour)
                visited.append(neighbour)
                next_level += 1
        cur_level -= 1
        if cur_level == 0:
            levels += 1
            cur_level = next_level
            next_level = 0
    return 0


def neighbours2(coord, matrix):  # it would be prettier to put a parameter into a single neighbours function, to pick whether it's part 1 or 2, but I don't feel like doing it
    alphabet = 'SabcdefghijklmnopqrstuvwxyzE'
    output = []
    y, x = coord[0], coord[1]
    if y > 0 and alphabet.index(matrix[y-1][x]) - alphabet.index(matrix[y][x]) >= -1:
        output.append([y-1, x])
    if y < len(matrix)-1 and alphabet.index(matrix[y+1][x]) - alphabet.index(matrix[y][x]) >= -1:
        output.append([y+1, x])
    if x > 0 and alphabet.index(matrix[y][x-1]) - alphabet.index(matrix[y][x]) >= -1:
        output.append([y, x-1])
    if x < len(matrix[0])-1 and alphabet.index(matrix[y][x+1]) - alphabet.index(matrix[y][x]) >= -1:
        output.append([y, x+1])
    return output


def part2():
    with open("input.txt") as file:
        matrix = [list(row) for row in file.read().split("\n")]
    for index, row in enumerate(matrix):
        if "E" in row:
            start = [index, row.index("E")]
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)
    levels = 1
    cur_level = 1
    next_level = 0
    while len(queue):
        for neighbour in neighbours2(queue.pop(0), matrix):
            if neighbour not in visited:
                if matrix[neighbour[0]][neighbour[1]] == "a":
                    return levels
                queue.append(neighbour)
                visited.append(neighbour)
                next_level += 1
        cur_level -= 1
        if cur_level == 0:
            levels += 1
            cur_level = next_level
            next_level = 0
    return 0


print(f"Part 1: {part1()}\nPart2: {part2()}")
