with open("input/day01.txt") as f:
    masses = [int(l.strip("\n")) // 3 - 2 for l in f.readlines()]


print(sum(masses))

masses2 = []
for mass in masses:
    t = mass
    m = mass
    while m // 3 - 2 >= 0:
        m = m // 3 - 2
        t += m
    masses2.append(t)

print(sum(masses2))
