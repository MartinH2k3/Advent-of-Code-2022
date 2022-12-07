class Folder:
    def __init__(self, parent):
        self.sub_dirs = []
        self.parent: Folder = parent
        self.value = 0


def write_file():
    with open("input.txt") as file:
        commands = list(i.split(" ") for i in filter(lambda x: x != "$ ls" and x[:3] != "dir", file.read().split("\n")))

    drive = Folder(None)
    cur_dir = drive

    for command in commands:
        if command[0] == "$":
            if command[-1] == "..":
                cur_dir.parent.value += cur_dir.value
                cur_dir = cur_dir.parent
            else:
                cur_dir.sub_dirs.append(Folder(cur_dir))
                cur_dir = cur_dir.sub_dirs[-1]
        else:
            cur_dir.value += int(command[0])
    while cur_dir != drive:
        cur_dir.parent.value += cur_dir.value
        cur_dir = cur_dir.parent
    return drive


def part1():
    def dfs(directory):
        for sub_dir in directory.sub_dirs:
            dfs(sub_dir)
        output[0] += directory.value * (directory.value < 100000)
    output = [0]
    drive = write_file()
    dfs(drive)
    return output[0]


def part2():
    def dfs(directory):
        for sub_dir in directory.sub_dirs:
            dfs(sub_dir)
        output[0] += (directory.value - output[0]) * (output[1] < directory.value < output[0])

    drive = write_file()
    output = [drive.value, drive.value - 40000000]
    dfs(drive)
    return output[0]


print(part2())
