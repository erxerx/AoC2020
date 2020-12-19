import numpy as np
#exps=['1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) )'.split(' ')]
exps=['1 + 2 * 3 + ( 4 * ( 5 + 6 ) )'.split(' ')]

def evalexp(inexp):
  print('eval:', inexp)
  argcnt = 0
  arg = [0,0,0]
  op = ''
  nest = 1
  accu = 0
  result = ''
  for i in range(len(inexp)):
    if ('0' <= inexp[i][0] and inexp[i][0] <= '9'):
      argcnt += 1
      arg[argcnt] = int(inexp[i])
      if argcnt == 1:
        print('int:(', argcnt, ') =', inexp[i])
      else:
        result = ' res =' + str(arg[1]) + op + str(arg[2])
        print(result)
        #return inexp[i]
    elif inexp[i][0] == '+':
      op = '+'
      print('op:', op)
      if argcnt == 2:
        print('return:+ ',[str(accu + int(inexp[i])), evalexp(inexp[i + 1:])])
        return [str(accu + int(inexp[i])), evalexp(inexp[i + 1:])]
    elif inexp[i][0] == '*':
      print('op:*', op)
      if argcnt == 2:
        print('return:* ',[str(accu + int(inexp[i])), evalexp(inexp[i + 1:])])
        return [str(accu * int(inexp[i])), evalexp(inexp[i + 1:])]
    elif inexp[i][0] == '(':
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