with open('d12.in', 'r') as f:
  content = f.read()
l = content.split('\n')
x = 0
y = 0
wx = 10
wy = -1

for i in l:
  op = i[0]
  val = int(i[1:])
  if op == 'N': wy -= val
  if op == 'E': wx += val
  if op == 'W': wx -= val
  if op == 'S': wy += val
  if op == 'R':
    for j in range(0, int(val/90)):
      wx, wy = -wy, wx
  if op == 'L':
    for j in range(0, int(val/90)):
      wx, wy = wy, -wx
  if op == 'F':
    x += val * wx
    y += val * wy
print(i, x,y, '|', wx, wy, '|', abs(x) + abs(y))