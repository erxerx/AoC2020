# from itertools import cycle
cups = list('389125467')
cups.extend([str(i + 1) for i in range(len(cups),1000000)])

def read_cup(ii):
    return cups[ii % len(cups)]


def write_cup(ii, val):
    cups[ii % len(cups)] = val


for turn in range(100):
    current = read_cup(turn)
    pickup = read_cup(turn + 1) + read_cup(turn + 2) + read_cup(turn + 3)
    rest = ''
    for i in range(len(cups) - 4):
        rest = rest + read_cup(turn + 4 + i)
    # rest = cups[(turn + 4):]
    dst = str(int(current) - 1)
    while not (dst in rest):
        dst = str(int(dst) - 1)
        if dst < min(rest): dst = max(rest)
    # cups = current + rest[:rest.index(dst) + 1] + pickup + rest[rest.index(dst) + 1:]
    pickup_add = 0
    for i in range(len(cups) - 4):
        write_cup(turn + 1 + i + pickup_add, rest[i])
        if rest[i] == dst:
            write_cup(turn + 2 + i, pickup[0])
            write_cup(turn + 3 + i, pickup[1])
            write_cup(turn + 4 + i, pickup[2])
            pickup_add = 3
            # rest = rest + read_char(cups, turn + 4 + i)
# print(cups)
# for i in range(len(cups) - 1):
#     print(read_cup(start + 1 + i), end='')
#
c1 = read_cup(cups.index('1') + 1)
c2 = read_cup(cups.index('1') + 2)
print(int(c1)*int(c2))
