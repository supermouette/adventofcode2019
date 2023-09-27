with open("input/day02.txt") as f:
    mem = [int(l) for l in f.readline().strip("\n").split(",")]


def run(mem, noun, verb):
    ops = mem[:]
    ops[1] = noun
    ops[2] = verb
    cur = 0
    while ops[cur] != 99:
        if ops[cur] == 1:
            ops[ops[cur + 3]] = ops[ops[cur + 1]] + ops[ops[cur + 2]]
        elif ops[cur] == 2:
            ops[ops[cur + 3]] = ops[ops[cur + 1]] * ops[ops[cur + 2]]
        else:
            raise ValueError("not implemented")
        cur += 4
    return ops[0]


print(run(mem, 12, 2))

for i in range(100):
    for j in range(100):
        if run(mem, i, j) == 19690720:
            print(i * 100 + j)
            break
