def part1():
    with open("input.txt") as file:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        error = 0
        for line in file.read().split("\n"):
            first_half = set()
            for letter in line[:len(line)//2]:
                first_half.add(letter)
            for letter in line[len(line)//2:]:
                if letter in first_half:
                    error += 1 + alphabet.index(letter)
                    break
        return error


def part2():
    with open("input.txt") as file:
        rucksacks = file.read().split("\n")
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        priorities = 0
        for i in range(0, len(rucksacks), 3):
            priorities += 1 + alphabet.index(set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2])).pop())
        return priorities


print(f"Part 1: {part1()}\nPart 2: {part2()}")

