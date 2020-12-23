with open('d19.in2', 'r') as f:
  content = f.read()
l = content.split('\n\n')
rules = {int(x.split(': ')[0]):x.split(': ')[1].replace('\n', '') for x in l[0].split('\n')}
exps = [x.replace('\n', '') for x in l[1].split('\n')]

def matches(inexp, ruleidx):
  #print('match?:', ruleidx, inexp)
  for oneseq in rules[ruleidx].split(' | '):
    #print('submatch?:', oneseq, inexp)
    i = 0
    fnd = True
    for onematch in oneseq.replace('"', '').split(' '):
      #if i >= len(inexp): return 0
      if ('0' <= onematch[0] and onematch[0] <= '9'):
        res = matches(inexp[i:], int(onematch))
        #print('in', ruleidx, 'from ', inexp[i:], ' read ', res, 'with', onematch)
        if not res:
          i = 0
          fnd = False
          break
        i += res
        continue
      else:
        if i >= len(inexp): return i
        if onematch != inexp[i]: return 0
      i += 1
    if fnd: return i
  return i  #result  # argstack[0]

summ = 0
for exp in exps:
  #print(exp)
  if matches(exp, 0) == len(exp):
    #print(exp, 'matches')
    summ += 1
print('part1:', summ)
