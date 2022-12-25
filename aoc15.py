import re
from time import time


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


def part1():
    with open("input.txt") as file:
        positions = file.read().split("\n")
        for line_index, line in enumerate(positions):
            sensor_coords = re.search(r"x=(-?\d+), y=(-?\d+)", line)
            bacon_coords = tuple(int(i) for i in re.search(r"x=(-?\d+), y=(-?\d+)", line[sensor_coords.end():]).groups())
            sensor_coords = tuple(int(i) for i in sensor_coords.groups())
            positions[line_index] = (sensor_coords, bacon_coords)

    output_intervals = []
    row = 2000000
    beacons_on_that_row = len(set([i[1] for i in filter(lambda x: x[1][1] == row, positions)]))

    for sensor, beacon in positions:
        manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        half_length = manhattan_distance - abs(sensor[1] - row)
        if half_length < 0:
            continue
        output_intervals.append([sensor[0]-half_length, sensor[0]+half_length+1])

    return sum(i[1]-i[0] for i in join_intervals(output_intervals)) - beacons_on_that_row

t1 = time()
print(part1())
t2 = time()
print((t2-t1)*4000000)