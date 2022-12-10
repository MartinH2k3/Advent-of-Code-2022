def part1():
    register, cycle, strength = 1, 0, 0
    with open("input.txt") as file:
        commands = file.read().split("\n")
    for command in commands:
        if command == "noop":
            cycle += 1
            if cycle % 40 == 20:
                strength += cycle * register
        else:
            if cycle % 40 == 18 or cycle % 40 == 19:
                strength += (cycle - cycle % 40 + 20) * register # scuffed rounding up, but works
            cycle += 2
            register += int(command.split(" ")[-1])
    return strength


print(f"Part 1: {part1()}")
