import numpy as np
exps=['1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) )'.split(' ')]

def evalexp(inexp):
  print('eval:', inexp)
  icnt = 0
  op = ''
  for i in range(len(inexp)):
    if ('0' <= inexp[i][0] and inexp[i][0] <= '9'):
      print('int:', inexp[i])
      icnt += 1
      if icnt == 2:
        if op == '+':
          print('return: ',x + int(inexp[i]))
          return str(x + int(inexp[i]))
        if op == '*':
          print('return: ',x * int(inexp[i]))
          return str(x * int(inexp[i]))
      x = int(inexp[i])
    if inexp[i][0] == '+':
      op = '+'
      print('op:', op)
    if inexp[i][0] == '*':
      op = '*'
      print('op:', op)
    if inexp[i][0] == '(':
      nest = 1
      for j in range(i + 1,len(inexp)):
        if inexp[j][0] == '(':
          nest += 1
        if inexp[j][0] == ')':
          nest -= 1
          if nest == 0:
            subeval = inexp[i + 1:j]
            print('subeval:', subeval)
            evalexp(subeval)

for exp in exps:
  evalexp(exp)