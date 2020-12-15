with open('d14.in', 'r') as f:
  content = f.read()
l = content.split('\n')
ll = [x.replace('= ', '').split(' ') for x in l]  #restore from file
mem = {}
for i in ll:
  op = i[0]
  val = i[1]
  if op == 'mask':
    mask = val
    floatbits = []
    for j in range(36):
      if mask[-1-j] == 'X': floatbits.append(j)
    #and_mask = int(val.replace('X','1'),2)
    or_mask = int(val.replace('X', '0'),2)
  if op[:3] == 'mem':
    adr = int(op[4:-1])
    #mem[adr] = (int(val) & and_mask) | or_mask
    cnt = 2 ** mask.count('X')
    for k in range(2 ** mask.count('X')):
      kk = k
      for j in range(mask.count('X')):
        adr &= (~ 2 ** floatbits[j]) # reset bit
        if kk & 1 : adr |= (2 ** floatbits[j]) # reset bit
        adr |= or_mask
        kk = kk >> 1
      mem[adr] = (int(val))
print(sum(mem.values()))
