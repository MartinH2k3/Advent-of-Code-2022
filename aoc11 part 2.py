from time import time


class Monke:
    def __init__(self, monkeys):
        self.monkeys: list[Monke] = monkeys
        self.inspected_count = 0
        self.divisors = []
        self.divisors_count = 0
        self.items = []
        self.operation_string = ""
        self.test = (0, 0, 0)

    def update(self):
        self.divisors = [monke.test[0] for monke in self.monkeys]
        self.divisors_count = len(self.divisors)
        self.items = [[int(item) % divisor for divisor in self.divisors] for item in self.items]

    def operation(self):
        for item in self.items:
            self.inspected_count += 1
            for sub_index in range(self.divisors_count):
                item[sub_index] = eval(self.operation_string.replace("old", str(item[sub_index]))) % self.divisors[sub_index]
            self.monkeys[self.test[(item[self.divisors.index(self.test[0])] != 0)+1]].items.append(item)
        self.items.clear()


def part2():
    with open("input.txt") as file:
        monkey_inputs = [[j.replace(" ", "") for j in i.split("\n")[1:]] for i in file.read().split("\n\n")]
    monkeys = []
    for monkey_input in monkey_inputs:
        monkeys.append(Monke(monkeys))
        monkeys[-1].items = monkey_input[0].replace("Startingitems:", "").split(",")
        monkeys[-1].operation_string = monkey_input[1].replace("Operation:new=", "")
        monkeys[-1].test = int(monkey_input[2].replace("Test:divisibleby", "")), int(monkey_input[3].replace("Iftrue:throwtomonkey", "")), int(monkey_input[4].replace("Iffalse:throwtomonkey", ""))
    for monkey in monkeys:
        monkey.update()
    for monke_round in range(10000):
        for monke in monkeys:
            monke.operation()
    a = sorted(monke.inspected_count for monke in monkeys)
    return a[-1] * a[-2]


print("Part 2: ", part2())
