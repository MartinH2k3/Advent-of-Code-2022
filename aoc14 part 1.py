def stone_line(point1: list[int, int], point2: list[int, int], matrix):
    y_dif = (point1[0] <= point2[0]) - (point1[0] > point2[0])
    x_dif = (point1[1] <= point2[1]) - (point1[1] > point2[1])
    for i in range(point1[0], point2[0] + y_dif, y_dif):
        matrix[point1[1]][i] = 1
    for i in range(point1[1], point2[1] + x_dif, x_dif):
        matrix[i][point1[0]] = 1
    return matrix


def drop_sand(matrix):
    sand_position = [50, 0]
    while sand_position[1] != len(matrix)-1:
        if not matrix[sand_position[1]+1][sand_position[0]]:
            sand_position[1] += 1
        elif (sand_position[0] != 0 or sand_position[0] != len(matrix) - 1) and not matrix[sand_position[1]+1][sand_position[0]-1]:
            sand_position[1] += 1
            sand_position[0] -= 1
        elif (sand_position[0] != 0 or sand_position[0] != len(matrix) - 1) and not matrix[sand_position[1]+1][sand_position[0]+1]:
            sand_position[1] += 1
            sand_position[0] += 1
        else:
            matrix[sand_position[1]][sand_position[0]] = 5
            return matrix
    return 0


def part1():
    with open("input.txt") as file:
        lines = [[[int(j.split(",")[0]) - 450, int(j.split(",")[1])] for j in i.split(" -> ")] for i in
                 file.read().split("\n")]
    matrix = [[0 for j in range(80)] for i in range(165)]
    for line in lines:
        for i in range(len(line) - 1):
            matrix = stone_line(line[i], line[i + 1], matrix)
    dropped = -1
    while matrix != 0:
        dropped += 1
        matrix = drop_sand(matrix)
    return dropped


print(f"Part 1: {part1()}")

