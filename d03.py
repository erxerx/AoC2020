with open('d03.in', 'r') as f:
  d = f.readlines()
#dd = [x.split(' ') for x in d]
pos = c = 0
for i in d[::2]:
  if i[pos % 31] == "#": c += 1
  pos += 1
print(c)