from itertools import permutations, product, combinations
from collections import defaultdict
from math import sqrt

edges = defaultdict(list)

with open('d20.in1', 'r') as f:
    content = f.read()
lcontent = content.split('\n\n')
tiles = {int(x.split(':')[0][5:]): x.split('\n')[1:11] for x in lcontent}
tlen = 10
glen = int(sqrt(len(tiles)))
grid = [[(0, 0)] * glen] * glen


def edge(tilenum, edgenum):
    if edgenum == 0: return tiles[tilenum][0]
    if edgenum == 1: return ''.join([tiles[tilenum][x][tlen - 1] for x in range(tlen)])
    if edgenum == 2: return tiles[tilenum][tlen - 1]
    if edgenum == 3: return ''.join([tiles[tilenum][x][0] for x in range(tlen)])
    if edgenum == 4: return tiles[tilenum][tlen - 1]
    if edgenum == 5: return ''.join([tiles[tilenum][tlen - x - 1][tlen - 1] for x in range(tlen)])
    if edgenum == 6: return tiles[tilenum][0]
    if edgenum == 7: return ''.join([tiles[tilenum][tlen - x - 1][0] for x in range(tlen)])


def chkgrid(grid):
    return True
    for y in range(glen - 1):
        for x in range(glen - 1):
            print(x, y)


def solvegrid(grid, available):
    if not chkgrid(grid): return False
    if len(available) == 0: return True
    trytile = available.pop()
    for orientation in range(8):
        grid.append((trytile, orientation))
        if solvegrid(grid, available):
            print('YESS')
        else:
            print('NOOO')


for tile in tiles.keys():
    for orientation in range(8):
        # print(edge(tile, orientation), tile, orientation)
        edges[edge(tile, orientation)].append((tile, orientation))

print(solvegrid([], list(tiles.keys())))

for tile in tiles.keys():
    fit = 0
    for orientation in range(8):
        fit += len(edges[edge(tile, orientation)])
    print(tile, fit)

orientations = list([range(4)] * glen * glen)
a = 0
for perm in zip(product(permutations(tiles.keys()), product(*orientations))):
    a += 1

print(a)
