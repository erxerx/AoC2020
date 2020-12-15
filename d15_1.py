#with open('d15.in1', 'r') as f:
#  content = f.read()
#l = content.split('\n')
#ll = [x.replace('= ', '').split(' ') for x in l]  #restore from file
mem = [0,3,6]
#mem = {}
for turn in range(len(mem),2019):
  last = mem[turn-1]
  if mem.count(last) == 1:
    mem.append(0)
    continue
  mem.append(turn - mem[:-1:-1].index(last) - 1)
print(last)