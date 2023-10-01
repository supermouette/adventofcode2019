with open("input/day05.txt") as f:
    mem = [int(l) for l in f.readline().strip("\n").split(",")]


def run(mem: list[int], input_val: list[int] = None, debug: bool = False):
    if input_val is None:
        input_val = []
    else:
        input_val = input_val[::-1]
    ops = mem[:]
    cur = 0
    while ops[cur] % 100 != 99:
        opcode = ops[cur] % 100
        if opcode in (1, 2, 7, 8):
            nb_param = 3
        elif opcode in (3, 4):
            nb_param = 1
        elif opcode in (5, 6):
            nb_param = 2

        modes = str(int(ops[cur] // 100))[::-1]
        if len(modes) < nb_param:
            modes += "0" * (nb_param - len(modes))
        args = []
        for i in range(nb_param):
            if modes[i] == "0":
                args.append(ops[ops[cur + i + 1]])
            elif modes[i] == "1":
                args.append(ops[cur + i + 1])
            else:
                raise ValueError(f"mode {modes[i]} not implemented")

        if debug:
            print("instructions :", ops[cur : cur + nb_param + 1])
            print("  mods :", modes)
            print("  args :", args)

        jump = False

        if opcode == 1:
            ops[ops[cur + 3]] = args[0] + args[1]
        elif opcode == 2:
            ops[ops[cur + 3]] = args[0] * args[1]
        elif opcode == 3:
            if len(input_val) == 0:
                val = int(input("opcde 3, please enter input value : "))
            else:
                val = input_val.pop()
            ops[ops[cur + 1]] = val
        elif opcode == 4:
            print(f"opcode 4 : {args[0]}")
        elif opcode == 5:
            if args[0] != 0:
                jump = True
                cur = args[1]
        elif opcode == 6:
            if args[0] == 0:
                jump = True
                cur = args[1]
        elif opcode == 7:
            ops[ops[cur + 3]] = 1 if args[0] < args[1] else 0
        elif opcode == 8:
            ops[ops[cur + 3]] = 1 if args[0] == args[1] else 0
        else:
            raise ValueError(f"opcode {ops[cur]} not implemented")
        if not jump:
            cur += nb_param + 1
        if debug:
            print(cur, ops)
    return ops[0]


print("part 1")
run(mem, [1])
print("part 2")
run(mem, [5])
