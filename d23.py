cups = [int(x) for x in '389125467']
for turn in range(100):
    current = cups[turn % len(cups)]
    pickup = cups[(turn + 1) % len(cups):(turn + 4) % len(cups)]
    rest = cups[(turn + 5) % len(cups):]
    dest = current - 1
    while not (dest in rest):
        dest -= 1
        if dest < min(rest): dest = max(rest)
    cups = [current] + rest[:rest.index(dest) + 1] + pickup + rest[rest.index(dest)+1:]
print()
