with open('d10.in', 'r') as f:
  content = f.read()
l = [int(x) for x in content.split('\n')]
l.sort()
l = [0,0,0] + l #+ [1000] # set edges
count=1
c1 = 0
c3 = 1
seqlen=0
for i in range(2,len(l)):
  #print(l[i], l[i] - l[i - 1])
  if (l[i] - l[i-1]) == 3: c3 += 1
  if (l[i] - l[i-1]) == 1:
    c1 += 1
    seqlen += 1
  else:
    if seqlen > 0:
      #print('cnt=',cnt)
      if seqlen == 2: count *=2
      if seqlen == 3: count *=4
      if seqlen == 4: count *=7
      seqlen = 0
print(c1,c3,c1*c3)
print(count)