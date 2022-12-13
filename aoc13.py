import ast  # I'm not gonna parse this manually


def compare(left, right):
    if type(left) == int and type(right) == int:
        return (left <= right) + (left < right)
    if type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]
    len_l = len(left)
    len_r = len(right)
    for i in range(min(len_l, len_r)):
        if not compare(left[i], right[i]):
            return False
        elif compare(left[i], right[i]) == 2:
            return 2
    return (len_l <= len_r) + (len_l < len_r)


def part1():
    with open("input.txt") as file:
        pairs = [[ast.literal_eval(j) for j in i.split("\n")] for i in file.read().split("\n\n")]

    output = 0
    for index, pair in enumerate(pairs):
        if compare(pair[0], pair[1]):
            output += index+1

    return output


def bubble_sort(packets):  # I'm just imagining this is the way bubble sort works like, never looked it up, just heard of it
    errors = 1
    while errors:
        errors = 0
        for index in range(1, len(packets)):
            if not compare(packets[index-1], packets[index]):
                errors += 1
                robert = packets[index]
                packets[index] = packets[index-1]
                packets[index-1] = robert
    return packets


def part2():
    with open("input.txt") as file:
        packets = [ast.literal_eval(i) for i in file.read().replace("\n\n", "\n").split("\n")]
    packets.append([[2]])
    packets.append([[6]])
    packets = bubble_sort(packets)
    return (packets.index([[2]])+1) * (packets.index([[6]])+1)


print(f"Part 1: {part1()}\nPart 2: {part2()}")