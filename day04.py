input_range = [264793, 803935]  # oh no


def is_valid(nb):
    nb_str = str(nb)
    check = False
    for i in range(1, len(nb_str)):
        if nb_str[i] < nb_str[i - 1]:
            return False
        if nb_str[i] == nb_str[i - 1]:
            check = True
    return check


def is_valid_2(nb):
    nb_str = str(nb)
    cpt = 0
    r = {}
    for i in range(1, len(nb_str)):
        if nb_str[i] < nb_str[i - 1]:
            return False
        if nb_str[i] == nb_str[i - 1]:
            r[nb_str[i]] = r.get(nb_str[i], 1) + 1
    a = list(r.values())
    a.sort()
    return len(a) > 0 and a[0] == 2


def next_val():
    pass


counter = 0
i = input_range[0]
while i <= input_range[1]:
    if is_valid(i):
        counter += 1
    i += 1

print(counter)

counter = 0
i = input_range[0]
while i <= input_range[1]:
    if is_valid_2(i):
        counter += 1
    i += 1

print(counter)
