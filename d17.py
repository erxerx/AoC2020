with open('d17.in1', 'r') as f:
  content = f.read()
l = content.split('\n')
lenn = max(len(l), len(l[0])) + 12
space = [['.' * lenn] * lenn ] * 12
nextspace = space[::]
ix = 7
iy = 7
z = 5
for dy in range(len(l)):
  y = iy + dy
  for dx in range(len(l[0])):
    x = ix + dx
    nextspace[z][y] = nextspace[z][y][:7] + l[dx] + nextspace[z][y][:6][9:]
    #if l[dy][dx] == '#':
    #  print(x,y,0)
    #  space[z][y][x] = '#'

wx = 10
