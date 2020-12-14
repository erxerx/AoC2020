with open('d02.tr', 'r') as f:
  d = f.readlines()
dd = [x.split(' ') for x in d]
c = 0
for i in dd:
  t = 0
  if i[4].rstrip('\n')[int(i[0]) - 1] == i[2]: t += 1
  if i[4].rstrip('\n')[int(i[1]) - 1] == i[2]: t += 1
  if t == 1: c += 1
print(c)