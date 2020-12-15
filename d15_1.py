mem = [0,3,6]
#mem = [5,1,9,18,13,8,0]
memdict = {mem[i]:i for i in range(len(mem)-1)}
#mem = {}
last = mem[len(mem)-1]
mem.pop()
for turn in range(len(memdict),2021):
  mem.append(last)
  if last == 0:
    memdict[turn - lastzero] = turn
    last = turn - lastzero
  elif last in memdict:
    memdict[last] = turn - memdict[last]
    last = turn - memdict[last]
  else:
    memdict[last] = turn
    lastzero = memdict[0]
    memdict[0] = turn + 1
    last = 0
  continue
  if mem.count(last) == 1:
    mem.append(0)
    continue
  a = mem[-2::-1]
  last = newnum
  mem.append(mem[-2::-1].index(last) + 1)
print(last)
