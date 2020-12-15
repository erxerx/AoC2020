#with open('d15.in1', 'r') as f:
#  content = f.read()
#l = content.split('\n')
#ll = [x.replace('= ', '').split(' ') for x in l]  #restore from file
mem = [5,1,9,18,13,8,0]
#mem = {}
for turn in range(len(mem),2021):
  last = mem[turn-1]
  if mem.count(last) == 1:
    mem.append(0)
    continue
  a = mem[-2::-1]
  mem.append(mem[-2::-1].index(last) + 1)
print(last)
