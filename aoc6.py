def both_parts(length):
    with open("input.txt") as file:
        text = file.read()
        for i in range(length, len(text)):
            if len(set(text[i - length:i])) == length:
                return i


print(f"Part 1: {both_parts(4)}\nPart 2: {both_parts(14)}")

