def part_one():
    opponent_values = ["A", "B", "C"]
    my_values = ["X", "Y", "Z"]
    with open("input.txt") as file:
        score = 0
        for line in file.read().split("\n"):
            my_turn = my_values.index(line[-1])
            opponent_turn = opponent_values.index(line[0])
            score += my_turn+1 + 6*(my_turn == (opponent_turn+1)%3) + 3*(my_turn == opponent_turn)
        return score


def part_two():
    values = ["A", "B", "C"]
    with open("input.txt") as file:
        score = 0
        for line in file.read().split("\n"):
            if line[-1] == "X":
                score += 1 + (values.index(line[0]) + 2) % 3
            elif line[-1] == "Y":
                score += 3 + 1 + values.index(line[0])
            elif line[-1] == "Z":
                score += 6 + 1 + (values.index(line[0]) + 1) % 3
        return score


print(f"Part 1: {part_one()}\nPart 2: {part_two()}")