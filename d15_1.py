#mem = [0, 3, 6]
mem = [5,1,9,18,13,8,0]
seen = {mem[i]: i for i in range(len(mem) - 1)}
lastseen = len(mem) - 1
last = mem[lastseen]
#mem.pop()
for turn in range(len(seen), 30000000 - 1):
    seen[last] = turn
#    mem.append(last)
    if last in seen:  # already seen number, next is diff with last seen turn
      next = turn - lastseen
    else:  # first time this number, next is zero. preserve last seen 0 turn
      next = 0
      lastzeroturn = seen[0]
    lastseen = turn if next == last else seen[next] if next in seen else turn + 1
    last = next
print(last)
