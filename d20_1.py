from collections import defaultdict
from itertools import permutations, product
from math import sqrt

edges = defaultdict(list)

with open('d20.in1', 'r') as f:
    content = f.read()
rec = content.split('\n\n')
tiles = {int(x.split(':')[0][5:]): x.split('\n')[1:11] for x in rec}
tile_len = 10
glen = int(sqrt(len(tiles)))
grid = [[(0, 0)] * glen] * glen


def edge(tile_num, edge_num):
    if edge_num == 0: return tiles[tile_num][0]
    if edge_num == 1: return ''.join([tiles[tile_num][x][tile_len - 1] for x in range(tile_len)])
    if edge_num == 2: return tiles[tile_num][tile_len - 1]
    if edge_num == 3: return ''.join([tiles[tile_num][x][0] for x in range(tile_len)])
    if edge_num == 4: return tiles[tile_num][tile_len - 1]
    if edge_num == 5: return ''.join([tiles[tile_num][tile_len - x - 1][tile_len - 1] for x in range(tile_len)])
    if edge_num == 6: return tiles[tile_num][0]
    if edge_num == 7: return ''.join([tiles[tile_num][tile_len - x - 1][0] for x in range(tile_len)])


def chk_grid():
    return True
    # for y in range(glen - 1):
    #    for x in range(glen - 1):
    #        print(x, y)


def solve_grid(available):
    global grid
    if not chk_grid(): return False
    if len(available) == 0: return True
    try_tile = available.pop()
    print('try_tile', try_tile)
    for loc_orientation in range(8):
        # ... grid.append((try_tile, loc_orientation))
        if solve_grid(available):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    for tile in tiles.keys():
        for orientation in range(8):
            # print(edge(tile, orientation), tile, orientation)
            edges[edge(tile, orientation)].append((tile, orientation))

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
    print(list(tiles.keys()))
