with open('d05.tr', 'r') as f:
  content = f.read()
l = content.split('\n')
ll = [x.replace('\n', ' ').split(' ') for x in l]
taken = [0] * 945
for i in ll:
  seat = int(i[0],2) * 8 + int(i[1],2)
  taken[seat] = 1

for i in range(36,944):
  if not taken[i]: print(i)
