def part1():
    with open("input.txt") as file:
        moves = [i.split(" ") for i in file.read().split('\n')]
    head = [0, 0]
    tail = [0, 0]
    visited = set()
    for move, value in moves:
        head[0] += ((move == "U") - (move == "D")) * int(value)
        head[1] += ((move == "R") - (move == "L")) * int(value)
        if abs(head[1] - tail[1]) <= 1 and abs(head[0] - tail[0]) <= 1:
            continue

        if head[0] != tail[0] and head[1] != tail[1]:
            tail[0] += tail[0] < head[0]
            tail[0] -= tail[0] > head[0]
            tail[1] += tail[1] < head[1]
            tail[1] -= tail[1] > head[1]
            visited.add(f"{tail[0]}-{tail[1]}")

        if head[1] == tail[1]:
            direction = 1 * (tail[0] < head[0]) + (-1) * (tail[0] > head[0])
            for i in range(tail[0], head[0], direction):
                visited.add(f"{tail[0]}-{tail[1]}")
                tail[0] += direction
            tail[0] -= direction

        if head[0] == tail[0]:
            direction = 1 * (tail[1] < head[1]) + (-1) * (tail[1] > head[1])
            for i in range(tail[1], head[1], direction):
                visited.add(f"{tail[0]}-{tail[1]}")
                tail[1] += direction
            tail[1] -= direction

    return len(visited)


print(f"Part 1: {part1()}")
