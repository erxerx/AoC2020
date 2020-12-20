with open('d18.in', 'r') as f:
  content = f.read()
l = content.split('\n')
exps = [x.replace('\n', '').split(' ') for x in l]  #restore from file

tests=[
  ['1 + 2 * 3 + 4 * 5 + 6', 71, 231],
  ['1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) )', 51, 51],
  ['2 * 3 + ( 4 * 5 )', 26, 46],
  ['5 + ( 8 * 3 + 9 + 3 * 4 * 3 )', 437, 1445],
  ['5 * 9 * ( 7 * 3 * 3 + 9 * 3 + ( 8 + 6 * 4 ) )', 12240, 669060],
  ['( ( 2 + 4 * 9 ) * ( 6 + 9 * 8 + 6 ) + 6 ) + 2 + 4 * 2', 13632, 23340]
]

def evalexp1(inexp):
  i = -1
#  print('eval:', inexp)
  opstack = []
  argstack = []
  result = 0
  while i < len(inexp) - 1:
    i += 1
    token = inexp[i]
    if ('0' <= token[0] and token[0] <= '9'):
      result = int(token)
      #print('int:', result)
      argstack.append(result)
    elif token == '(':
      nest = 1
      for j in range(i + 1,len(inexp)):
        if inexp[j][0] == '(':
          nest += 1
        if inexp[j][0] == ')':
          nest -= 1
          if nest == 0:
            subeval = inexp[i + 1:j]
            result = evalexp1(subeval)
            #print('subeval:', subeval, ' res = ', result)
            argstack.append(result)
            i = j
            break
    elif token == '+':
      #print('op: +');
      opstack.append('+')
    elif token == '*':
      #print('op: *');
      opstack.append('*')
    if len(argstack) == 2:
      ops = opstack.pop()
      if ops == '+':
        #print('return: ', argstack[0], ' -> ', argstack[0] + argstack[1])
        result = argstack.pop() + argstack.pop()
      elif ops == '*':
        #print('return: ', argstack[0], ' -> ', argstack[0] * argstack[1])
        result = argstack.pop() * argstack.pop()
      argstack.append(result)
  return argstack.pop()  #result  # argstack[0]

def evalexp2(inexp):
  i = -1
  print('eval:', inexp)
  opstack = []
  argstack = []
  result = 0
  while i < len(inexp) - 1:
    i += 1
    token = inexp[i]
    if ('0' <= token[0] and token[0] <= '9'):
      result = int(token)
      #print('int:', result)
      argstack.append(result)
    elif token == '(':
      nest = 1
      for j in range(i + 1,len(inexp)):
        if inexp[j][0] == '(':
          nest += 1
        if inexp[j][0] == ')':
          nest -= 1
          if nest == 0:
            subeval = inexp[i + 1:j]
            result = evalexp2(subeval)
            #print('subeval:', subeval, ' res = ', result)
            argstack.append(result)
            i = j
            break
    elif token == '+':
      #print('op: +');
      opstack.append('+')
      continue
    elif token == '*':
      #print('op: *');
      opstack.append('*')
      continue
    if len(argstack) > 1 and opstack[-1] == '+':
      ops = opstack.pop()
      if ops == '+':
        #print('return: ', argstack[0], ' -> ', argstack[0] + argstack[1])
        result = argstack.pop() + argstack.pop()
      elif ops == '*':
        #print('return: ', argstack[0], ' -> ', argstack[0] * argstack[1])
        result = argstack.pop() * argstack.pop()
      argstack.append(result)
  return argstack.pop()  #result  # argstack[0]

for test in tests:
  res1 = evalexp1(test[0].split(' '))
  res2 = evalexp2(test[0].split(' '))
  print(test[0], '\t', end='')
  if res1 == test[1]:
    print('1. OK:', res1, '\t', end='')
  else:
    print('1.NOK: was ', res1, ' expected ', test[1], '\t', end='')
  if res2 == test[2]:
    print('2. OK:', res2)
  else:
    print('2.NOK: was ', res2, ' expected ', test[2], '\t', end='')
  print()

#summ1 = 0
#summ2 = 0
#for exp in exps:
#  summ1 += evalexp1(exp)
#  summ2 += evalexp2(exp)
#print('part1:', summ1)
#print('part2:', summ2)