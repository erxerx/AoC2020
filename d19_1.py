with open('d19.in1', 'r') as f:
  content = f.read()
l = content.split('\n\n')
rules = [x[3:].replace('\n', '') for x in l[0].split('\n')]  #restore from file
tests = [x.replace('\n', '') for x in l[1].split('\n')]  #restore from file

def matches(inexp, ruleidx):
  print('match?:', ruleidx, inexp)
  result = False
  for oneseq in rules[ruleidx].split('|'):
    print('submatch?:', oneseq)
    i = -1
    while i < len(inexp) - 1:
      i += 1
      token = inexp[i]
      for onerule in oneseq.split(' '):
        if ('0' <= onerule and onerule <= '9'):
          res = matches(inexp[i:],int(onerule))
          print(onerule, res)
        if onerule != token: return False
  return True  #result  # argstack[0]

for test in tests:
  print(test, '\t', matches(test, 0))

#summ1 = 0
#summ2 = 0
#for exp in exps:
#  summ1 += evalexp1(exp)
#  summ2 += evalexp2(exp)
#print('part1:', summ1)
#print('part2:', summ2)