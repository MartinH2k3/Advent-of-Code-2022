def parts():
    register, cycle, strength = 1, 0, 0
    with open("input.txt") as file:
        commands = file.read().split("\n")

    display = [[' ' for j in range(40)]for i in range(6)]
    for command in commands:
        if command == "noop":
            if cycle % 40 in range(register-1, register+2):
                display[cycle // 40][cycle % 40] = "█"
            cycle += 1
            if cycle % 40 == 20:
                strength += cycle * register
        else:
            if cycle % 40 == 18 or cycle % 40 == 19:
                strength += (cycle - cycle % 40 + 20) * register  # scuffed rounding up, but works
            for i in range(2):
                if cycle % 40 in range(register-1, register+2):
                    display[cycle // 40][cycle % 40] = "█"
                cycle += 1
            register += int(command.split(" ")[-1])
    return strength, '\n'.join(''.join(j) for j in display)


print(f"Part 1: {parts()[0]}\nPart 2:\n{parts()[1]}")
