from itertools import permutations, product
with open('d20.in1', 'r') as f:
  content = f.read()
lcontent = content.split('\n\n')
tiles = { int(x.split(':')[0][5:]):x.split('\n')[1:11] for x in lcontent }
tlen = 10
glen = 3
grid = [ [0] * glen ] * glen

def edge (tilenum,edgenum):
  if edgenum == 0: return tiles[tilenum][0]
  if edgenum == 1: return ''.join([tiles[tilenum][x][tlen - 1] for x in range(tlen)])
  if edgenum == 2: return tiles[tilenum][tlen - 1]
  if edgenum == 3: return ''.join([tiles[tilenum][x][0] for x in range(tlen)])

def chkgrid():
  for y in range(glen - 1):
    for x in range(glen - 1):
      print(x,y)


aa = product(tiles.keys(), [0,1,2,3])
#for perm in (permutations(tiles.keys())):
for perm in product(tiles.keys(), [0,1,2,3]):
  print(perm)