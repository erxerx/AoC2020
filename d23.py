from time import time
# cups = list('389125467')
# cups = list('58427369')
last_pointer = None


class Node:
    def __init__(self, data):
        self.item = data
        if data == 7: self.ref = cups
        else: self.ref = None

    def insert_at_end(self, data):
        global last_pointer
        new_node = Node(data)
        if self.ref is None:
            self.ref = new_node
            last_pointer = new_node
            return
        n = last_pointer
        # while n.ref is not None:
        #     n = n.ref
        n.ref = new_node
        last_pointer = new_node


cups = Node(3)


for i in '89125467':  # '57623984':
    cups.insert_at_end(int(i))
# for i in range(10, 11):
#    cups.insert_at_end(int(i))


start = time()
last_pointer = cups
for turn in range(10):
    current = last_pointer
    current_ref = last_pointer.ref
    pickup = [last_pointer.ref.item] + [last_pointer.ref.ref.item] + [last_pointer.ref.ref.ref.item]
    dst = current.item - 1
    while dst in pickup:
        dst -= 1
        if dst < 1: dst = 9
    last_pointer.ref = last_pointer.ref.ref.ref.ref
    seek = last_pointer.ref
    for i in range(10):
        if seek.item == dst:
            save_ref = seek.ref
            seek.ref = current_ref
            seek.ref.ref.ref.ref = save_ref
            break
        seek = current.ref
    last_pointer = current.ref
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
print(f"Time : {time() - start} seconds")
print(cups)
# for i in range(len(cups) - 1):
#     print(read_cup(start + 1 + i), end='')
# part1 ['9', '1', '6', '7', '3', '8', '4', '5', '2']
c1 = read_cup(cups.index('1') + 1)
c2 = read_cup(cups.index('1') + 2)
print(c1, c2, int(c1)*int(c2))
