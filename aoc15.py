import re


def join_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    output = []
    current = intervals[0]
    for interval in intervals:
        if current[1] >= interval[0]:
            if current[1] < interval[1]:
                current[1] = interval[1]
        else:
            output.append(current)
            current = interval
    output.append(current)
    return output


def solution():
    with open("input.txt") as file:
        positions = file.read().split("\n")
        for line_index, line in enumerate(positions):
            sensor_coords = re.search(r"x=(-?\d+), y=(-?\d+)", line)
            bacon_coords = tuple(int(i) for i in re.search(r"x=(-?\d+), y=(-?\d+)", line[sensor_coords.end():]).groups())
            sensor_coords = tuple(int(i) for i in sensor_coords.groups())
            positions[line_index] = (sensor_coords, bacon_coords)

    def part1(positions_in_func):
        output_intervals = []
        row = 2000000
        beacons_on_that_row = len(set([i[1] for i in filter(lambda x: x[1][1] == row, positions_in_func)]))

        for sensor, beacon in positions_in_func:
            manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            half_length = manhattan_distance - abs(sensor[1] - row)
            if half_length < 0:
                continue
            output_intervals.append([sensor[0] - half_length, sensor[0] + half_length + 1])

        return sum(i[1] - i[0] for i in join_intervals(output_intervals)) - beacons_on_that_row

    def part2(positions_in_func):
        max_row = 4000000
        sensor_and_manhattan = list(map(lambda x: (x[0], abs(x[0][0] - x[1][0]) + abs(x[0][1] - x[1][1])), positions_in_func))
        for row in range(max_row):
            output_intervals = []
            for sensor, manhattan_distance in sensor_and_manhattan:
                half_length = manhattan_distance - abs(sensor[1] - row)
                if half_length < 0:
                    continue
                output_intervals.append([(sensor[0] - half_length) * ((sensor[0] - half_length) > 0), ((sensor[0] + half_length + 1) > max_row) * max_row + (sensor[0] + half_length + 1) * ((sensor[0] + half_length + 1) <= max_row)])
            if join_intervals(output_intervals) != [[0, max_row]]:
                return join_intervals(output_intervals)[0][1]*4000000 + row
        return sensor_and_manhattan

    print(f"Part 1: {part1(positions)}\nPart 2: {part2(positions)}")


solution()
