tests=[
  ['1 + 2',3],
  ['1 + 2 * 3 + 4 * 5 + 6', 71],
  ['1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) )', 51],
  ['2 * 3 + ( 4 * 5 )', 26],
  ['5 + ( 8 * 3 + 9 + 3 * 4 * 3 )', 437],
  ['5 * 9 * ( 7 * 3 * 3 + 9 * 3 + ( 8 + 6 * 4 ) )', 12240],
  ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632]
]

def evalexp(inexp):
  i = -1
  print('eval:', inexp)
  icnt = 0
  opstack = []
  argstack = []
  result = 0
  while i < len(inexp) - 1:
    i += 1
    token = inexp[i]
    if ('0' <= token[0] and token[0] <= '9'):
      icnt += 1
      result = int(token)
      print('int: (', icnt, ') =', result)
      argstack.append(result)
    elif token == '(':
      token = ''
      nest = 1
      for j in range(i + 1,len(inexp)):
        if inexp[j][0] == '(':
          nest += 1
        if inexp[j][0] == ')':
          nest -= 1
          if nest == 0:
            subeval = inexp[i + 1:j]
            result = evalexp(subeval)
            print('subeval:', subeval, ' res = ', result)
            argstack.append(result)
            icnt += 1
            break
    elif token == '+':
      print('op: +'); opstack.append('+')
    elif token == '*':
      print('op: *'); opstack.append('*')
    if len(argstack) == 2:
      ops = opstack.pop()
      if ops == '+':
        print('return: ', argstack[0], ' -> ', argstack[0] + argstack[1])
        result = argstack.pop() + argstack.pop()
      elif ops == '*':
        print('return: ', argstack[0], ' -> ', argstack[0] * argstack[1])
        result = argstack.pop() * argstack.pop()
      icnt = 1
      argstack.append(result)
  return argstack.pop()  #result  # argstack[0]

for test in tests:
  res = evalexp(test[0].split(' '))
  if res == test[1]:
    print(' OK:', test, res)
  else:
    print('NOK:', test, res)