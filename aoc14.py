def stone_line(point1: list[int, int], point2: list[int, int], matrix):
    y_dif = (point1[0] <= point2[0]) - (point1[0] > point2[0])
    x_dif = (point1[1] <= point2[1]) - (point1[1] > point2[1])
    for i in range(point1[0], point2[0] + y_dif, y_dif):
        matrix[i][point1[1]] = 1
    for i in range(point1[1], point2[1] + x_dif, x_dif):
        matrix[point1[0]][i] = 1
    return matrix


def part1():
    with open("input.txt") as file:
        lines = [[[int(j.split(",")[0]) - 440, int(j.split(",")[1])] for j in i.split(" -> ")] for i in
                 file.read().split("\n")]
    matrix = [[0 for j in range(200)] for i in range(100)]
    for line in lines:
        for i in range(len(line) - 1):
            matrix = stone_line(line[i], line[i + 1], matrix)
    return "\n".join("".join(str(j) for j in i) for i in matrix)


print(part1())
