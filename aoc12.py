def get_neighbours(y_pos, x_pos, matrix, visited):
    alphabet = 'SabcdefghijklmnopqrstuvwxyzE'
    output = []

    if y_pos > 0 and alphabet.index(matrix[y_pos - 1][x_pos]) - alphabet.index(matrix[y_pos][x_pos]) <= 1:
        cur_pos = [y_pos - 1, x_pos]
        if cur_pos not in visited:
            output.append(cur_pos)

    if y_pos < len(matrix)-1 and alphabet.index(matrix[y_pos + 1][x_pos]) - alphabet.index(matrix[y_pos][x_pos]) <= 1:
        cur_pos = [y_pos + 1, x_pos]
        if cur_pos not in visited:
            output.append(cur_pos)

    if x_pos > 0 and alphabet.index(matrix[y_pos][x_pos - 1]) - alphabet.index(matrix[y_pos][x_pos]) <= 1:
        cur_pos = [y_pos, x_pos - 1]
        if cur_pos not in visited:
            output.append(cur_pos)
    print(alphabet.index(matrix[y_pos][x_pos + 1]), alphabet.index(matrix[y_pos][x_pos]))
    if x_pos < len(matrix[0]-1) and alphabet.index(matrix[y_pos][x_pos + 1]) - alphabet.index(matrix[y_pos][x_pos]) <= 1:
        cur_pos = [y_pos, x_pos + 1]
        if cur_pos not in visited:
            output.append(cur_pos)

    return output


def search(branches, matrix, visited, final_pos, steps):
    for branch in branches:
        visited.append(branch)
    next_wave = []
    for branch in branches:
        next_wave += get_neighbours(branch[0], branch[1], matrix, visited)
    if final_pos in next_wave:
        return steps
    else:
        steps = search(next_wave, matrix, visited, final_pos, steps+1)


def part1():
    with open("input.txt") as file:
        matrix = [list(row) for row in file.read().split("\n")]
    for index, row in enumerate(matrix):
        if "S" in row:
            start = [index, row.index("S")]
        if "E" in row:
            end = [index, row.index("E")]

    return search([start], matrix, [], end, 1)


print(part1())
