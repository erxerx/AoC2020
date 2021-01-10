from time import time


class Node:
    def __init__(self, data):
        self.label = data
        self.next = None

    def insert_at_end(self, data):
        global last_inserted
        new_node = Node(data)
        last_inserted.next = new_node
        last_inserted = new_node


start = time()
cups = Node(3)  # first cup
last_inserted = cups
for i in '89125467':  # ... and the rest '57623984':
    cups.insert_at_end(int(i))
for i in range(10, 1000001):  # add to end up to x
    cups.insert_at_end(int(i))
last_inserted.next = cups
current = cups
for turn in range(1000):
    current_next = current.next
    pickup = [current_next.label] + [current_next.next.label] + [current_next.next.next.label]
    dst = current.label - 1
    if dst < 1: dst = 1000000
    while dst in pickup:
        dst -= 1
        if dst < 1: dst = 1000000
    current.next = current_next.next.next.next
    seek = current.next
    while seek.label != dst: seek = seek.next
    save_next = seek.next
    seek.next = current_next
    seek.next.next.next.next = save_next
    current = current.next
    #
    #
    # for i in range(len(cups) - 4):
    #     rest = rest + read_cup(turn + 4 + i)
    # # rest = cups[(turn + 4):]
    # # cups = current + rest[:rest.index(dst) + 1] + pickup + rest[rest.index(dst) + 1:]
    # pickup_add = 0
    # for i in range(len(cups) - 4):
    #     write_cup(turn + 1 + i + pickup_add, rest[i])
    #     if rest[i] == dst:
    #         write_cup(turn + 2 + i, pickup[0])
    #         write_cup(turn + 3 + i, pickup[1])
    #         write_cup(turn + 4 + i, pickup[2])
    #         pickup_add = 3
    #         # rest = rest + read_char(cups, turn + 4 + i)
seek = cups
while seek.label != 1: seek = seek.next
after_one = seek.next
# while after_one.label != 1:
#     print(after_one.label, end='')
#     after_one = after_one.next
# 58427369
print(after_one.label, after_one.next.label, after_one.label * after_one.next.label)
print(f"\nTime : {time() - start} seconds")
# Time : 4.601478576660156e-05 seconds
