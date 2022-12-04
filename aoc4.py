def part1():
    with open("input.txt") as file:
        pairs = [[[int(i) for i in elf.split("-")] for elf in pair.split(",")] for pair in file.read().split("\n")]
    return sum(not (((pair[0][0] < pair[1][0]) and (pair[0][1] < pair[1][1])) or ((pair[0][0] > pair[1][0]) and (pair[0][1] > pair[1][1]))) for pair in pairs)


def part2():
    with open("input.txt") as file:
        pairs = [[[int(i) for i in elf.split("-")] for elf in pair.split(",")] for pair in file.read().split("\n")]
    return sum((pair[0][0] <= pair[1][0] <= pair[0][1]) or (pair[1][0] <= pair[0][0] <= pair[1][1]) for pair in pairs)


print("Part1:", part1())
print("Part2:", part2())
