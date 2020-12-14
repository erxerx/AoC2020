with open('d06.in', 'r') as f:
  content = f.read()
l = content.split('\n\n')
ll = [x.replace('\n', ' ').split(' ') for x in l]
c = 0
for i in ll:
  cnt=[0] * 44
  for j in i:
    for k in j:
      cnt[ord(k)-97] += 1
  c += len([x for x in cnt if x == len(i)])
print(c)
