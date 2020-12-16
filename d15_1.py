mem = [0, 3, 6]
# mem = [5,1,9,18,13,8,0]
seen = {mem[i]: i for i in range(len(mem) - 1)}
# mem = {}
last = mem[len(mem) - 1]
mem.pop()
for turn in range(len(seen), 2021):
    mem.append(last)
    if last == next:
        next = 1
    if last == 0:
      next = turn - lastzeroturn
    elif last in seen:  # already seen number, next is diff with last seen turn
      next = turn - lastseen
    else:  # first time this number, next is zero. preserve last seen 0 turn
      next = 0
      lastzeroturn = seen[0]
    lastseen = seen[next]
    seen[next] = turn
    last = next
print(last)
