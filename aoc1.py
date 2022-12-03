print(sum(sorted([sum([int(j) for j in i.split("\n")]) for i in open("input.txt").read().split("\n\n")], reverse=True)[:3]))
# change 3 to 1, for first part
