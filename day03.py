import matplotlib.pyplot as plt

with open("input/day03.txt") as f:
    ws = [l.strip("\n").split(",") for l in f.readlines()]

cs = [set([0]), set([0])]
last_p = [0, 0]
direction = {"R": 1j, "U": 1, "L": -1j, "D": -1}
h = [[0], [0]]
for i in range(len(ws)):
    for m in ws[i]:
        d = direction[m[0]]
        mvmt = [last_p[i] + c * d for c in range(1, 1 + int(m[1:]))]
        h[i] += mvmt
        cs[i] |= set(mvmt)
        last_p[i] = mvmt[-1]

intersect = []
i_1 = []
for i in range(len(h[0])):
    if h[0][i] in cs[1]:
        intersect.append(abs(h[0][i].real) + abs(h[0][i].imag))
        i_1.append([i, h[0][i]])

intersect.sort()

print(intersect[1])


i_2 = []
for i in range(len(h[1])):
    if h[1][i] in cs[0]:
        i_2.append([i, h[1][i]])

i_3 = []

for i in i_1:
    for j in i_2:
        if i[1] == j[1]:
            i_3.append(i[0] + j[0])

i_3.sort()
print(i_3[1])


plt.plot([i.imag for i in h[0]], [i.real for i in h[0]], color="red")
plt.plot([i.imag for i in h[1]], [i.real for i in h[1]], color="blue")
plt.show()
