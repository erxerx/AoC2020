from time import time
next_cup = {1: None}
last_inserted = 1


def add_cup(label):
    global last_inserted
    next_cup[last_inserted] = label
    last_inserted = label


start = time()
for i in '57623984':  # ... and the rest (ex '89125467')
    add_cup(int(i))
for i in range(10, 1000001):  # add to end up to x
    add_cup(int(i))
next_cup[last_inserted] = 1
print(f"List created : {time() - start} seconds")
# List created : 0.1917097568511963 seconds
current = 1
for turn in range(10000000):
    current_next = next_cup[current]
    pickup = [current_next] + [next_cup[current_next]] + [next_cup[next_cup[current_next]]]
    dst = current - 1
    if dst < 1: dst = 1000000
    while dst in pickup:
        dst -= 1
        if dst < 1: dst = 1000000
    next_cup[current] = next_cup[next_cup[next_cup[current_next]]]
    dst_next = next_cup[dst]
    next_cup[dst] = current_next
    next_cup[next_cup[next_cup[current_next]]] = dst_next
    current = next_cup[current]
# after_one = next_cup[1]
# while after_one != 1:
#     print(after_one, end='')
#     after_one = next_cup[after_one]
# part1: 58427369
print(next_cup[1], next_cup[next_cup[1]], next_cup[1] * next_cup[next_cup[1]])
# part2: 294528 377070 111057672960
print(f"\nTime : {time() - start} seconds")
#
# Time : 9.429563999176025 seconds
