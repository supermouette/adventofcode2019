# example :
# COM)B
# B)C
# C)D

with open("input/day06.txt") as f:
    orbites = [l.strip("\n").split(")") for l in f.readlines()]

o_count = {"COM": 0}
cpt = 0
old_count = 0
while old_count != len(o_count):
    old_count = len(o_count)
    cpt += 1
    for o in orbites:
        if o[0] in o_count:
            o_count[o[1]] = o_count[o[0]] + 1

print(cpt)

# part1
print(sum(o_count.values()))

# part2
o_map = {}

for o in orbites:
    o_map[o[1]] = o[0]

you_list = ["YOU"]
san_list = ["SAN"]

o = "YOU"
while o != "COM":
    o = o_map[o]
    you_list.append(o)

o = "SAN"
while o != "COM":
    o = o_map[o]
    san_list.append(o)

you_list = you_list[::-1]
san_list = san_list[::-1]

for i in range(len(you_list)):
    if you_list[i] != san_list[i]:
        print(i, you_list[i - 1])
        break

print(len(san_list) + len(you_list) - 2 * i - 2)
