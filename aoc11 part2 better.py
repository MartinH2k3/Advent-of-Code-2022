from math import lcm


class Monke:
    def __init__(self, monkeys):
        self.monkeys: list[Monke] = monkeys
        self.inspected_count = 0
        self.items = []
        self.operation_string = ""
        self.test = (0, 0, 0)

    def operation(self, divisor_lcm):
        for item in self.items:
            self.inspected_count += 1
            item = eval(self.operation_string.replace("old", item)) % divisor_lcm
            self.monkeys[self.test[(item % self.test[0] != 0)+1]].items.append(str(item))
        self.items.clear()


def part1():
    with open("input.txt") as file:
        monkey_inputs = [[j.replace(" ", "") for j in i.split("\n")[1:]] for i in file.read().split("\n\n")]
    monkeys = []
    common_multiple = 1
    for monkey_input in monkey_inputs:
        monkeys.append(Monke(monkeys))
        monkeys[-1].items = monkey_input[0].replace("Startingitems:", "").split(",")
        monkeys[-1].operation_string = monkey_input[1].replace("Operation:new=", "")
        monkey_mod = int(monkey_input[2].replace("Test:divisibleby", ""))
        common_multiple = lcm(common_multiple, monkey_mod)
        monkeys[-1].test = monkey_mod, int(monkey_input[3].replace("Iftrue:throwtomonkey", "")), int(monkey_input[4].replace("Iffalse:throwtomonkey", ""))
    for i in range(10000):
        for monke in monkeys:
            monke.operation(common_multiple)
    a = sorted(monke.inspected_count for monke in monkeys)
    return a[-1] * a[-2]


print("Part 1: ", part1())

