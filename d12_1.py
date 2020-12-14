with open('d12.in', 'r') as f:
  content = f.read()
l = content.split('\n')
# ll = [x.replace('\n', '').split(' ') for x in l]  #restore from file
direction = 'ESWN'
x = 0
y = 0
shipdir = 'E'
op = 'F'
val = 0

def calc_move():
  global x, y, val
  if op == 'N': y -= val
  if op == 'E': x += val
  if op == 'W': x -= val
  if op == 'S': y += val

for i in l:
  #print(i)
  op = i[0]
  val = int(i[1:])
  calc_move()
  if op == 'R': shipdir = direction[(direction.index(shipdir) + int(val/90)) % 4]
  if op == 'L': shipdir = direction[(direction.index(shipdir) - int(val/90)) % 4]
  if op == 'F': op = shipdir; calc_move()

print(shipdir,x,y, abs(x) + abs(y))