with open('d08.in', 'r') as f:
  content = f.read()
l = content.split('\n')
for ch in range(len(l)):
  ll = [x.replace('\n', '').split(' ') for x in l]  #restore from file
  covered = [0] * (len(ll) + 11)
  acc = 0
  ip = 0
  if ll[ch][0] == 'nop': ll[ch][0] = 'jmp'
  elif ll[ch][0] == 'jmp': ll[ch][0] = 'nop'
  while not covered[ip]:
    if ip >= len(l):
      print(acc)
      break
    covered[ip] = 1
    if ll[ip][0] == 'nop': ip += 1; continue
    if ll[ip][0] == 'acc': acc += int(ll[ip][1]); ip += 1; continue
    if ll[ip][0] == 'jmp': ip += int(ll[ip][1]); continue
    print('Unknown op'); break