with open('d09.in', 'r') as f:
  content = f.read()
l = [int(x) for x in content.split('\n')]
pre=25
for i in range(pre,len(l)):
  exist = 0
  for j in range(1,pre):
    if (l[i] - l[i-j]) in l[max(0,i-j-pre):i-j]:
      exist = 1
      break
  if not exist:
    print(l[i])
    summa=l[i]  #18272118
for i in range(len(l)):
  j=i+1
  while sum(l[i:j]) < summa: j += 1
  if sum(l[i:j]) == summa:
    print(min(l[i:j]) + max(l[i:j]))
    break
