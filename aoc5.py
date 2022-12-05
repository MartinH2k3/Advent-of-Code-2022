pillars = ['bvsntchq', 'wdbg', 'fwrtsqb', 'lgwszjdn', 'mpdvf', 'fwj', 'lnqbjv', 'gtrcjqsn', 'jsqcwdm']
# pillars = ["zn", "mcd", "p"]


def part1():
    with open("input.txt") as file:
        lines = [[int(i) for i in ''.join((''.join(''.join(line.split("move ")).split("to "))).split("from ")).split(' ')] for line in file.read().split("\n")]
    for line in lines:
        count = line[0]

        pillars[line[2] - 1] += pillars[line[1]-1][-count:][::-1]
        pillars[line[1] - 1] = pillars[line[1]-1][:-count]
    return pillars


def part2():
    with open("input.txt") as file:
        lines = [[int(i) for i in ''.join((''.join(''.join(line.split("move ")).split("to "))).split("from ")).split(' ')] for line in file.read().split("\n")]
    for line in lines:
        count = line[0]

        pillars[line[2] - 1] += pillars[line[1]-1][-count:]
        pillars[line[1] - 1] = pillars[line[1]-1][:-count]
    return pillars


print(''.join(i[-1] for i in part2()))