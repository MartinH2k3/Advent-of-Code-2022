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
            print(index+1)
            output += index+1

    return output


print(part1())