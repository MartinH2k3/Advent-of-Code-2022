def move_tail_closer(head, tail):
    if abs(head[1] - tail[1]) <= 1 and abs(head[0] - tail[0]) <= 1:
        return tail
    tail[0] += tail[0] < head[0]
    tail[0] -= tail[0] > head[0]
    tail[1] += tail[1] < head[1]
    tail[1] -= tail[1] > head[1]
    return tail


def part1():
    with open("input.txt") as file:
        moves = [i.split(" ") for i in file.read().split('\n')]
    head = [0, 0]
    tail = [0, 0]
    visited = set()
    for move, value in moves:
        for step in range(int(value)):
            head[0] += ((move == "U") - (move == "D"))
            head[1] += ((move == "R") - (move == "L"))
            tail = move_tail_closer(head, tail)
            visited.add(f"{tail[0]}/{tail[1]}")
    return len(visited)


def part2():
    with open("input.txt") as file:
        moves = [i.split(" ") for i in file.read().split('\n')]
    rope = [[0, 0] for i in range(10)]
    visited = set()
    for move, value in moves:
        for step in range(int(value)):
            rope[0][0] += ((move == "U") - (move == "D"))
            rope[0][1] += ((move == "R") - (move == "L"))
            for knot_index in range(1, len(rope)):
                rope[knot_index] = move_tail_closer(rope[knot_index-1], rope[knot_index])
            visited.add(f"{rope[-1][0]}/{rope[-1][1]}")
    return len(visited)


print(f"Part 1: {part1()}\nPart 2: {part2()}")
