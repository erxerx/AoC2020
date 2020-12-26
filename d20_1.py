from collections import defaultdict
from math import sqrt
# globals
edges = defaultdict(list)


def edge(tile_num, orientation, edge_num):  # return tile edge
    if orientation == 0:
        if edge_num == 0: return tiles[tile_num][0]
        if edge_num == 1: return ''.join([tiles[tile_num][x][tile_len - 1] for x in range(tile_len)])
        if edge_num == 2: return tiles[tile_num][tile_len - 1]
        if edge_num == 3: return ''.join([tiles[tile_num][x][0] for x in range(tile_len)])
    else:
        if edge_num == 0: return tiles[tile_num][tile_len - 1]
        if edge_num == 1: return ''.join([tiles[tile_num][tile_len - x - 1][tile_len - 1] for x in range(tile_len)])
        if edge_num == 2: return tiles[tile_num][0]
        if edge_num == 3: return ''.join([tiles[tile_num][tile_len - x - 1][0] for x in range(tile_len)])


def ok_tile(tile_pos, tile_num, orientation):
    if tile_num >= glen:  # from 2nd row check that tile's upper edge matches previous row's lower edge
        if edge(tile_num, orientation, 0) != edge(grid[tile_pos - glen], orientation, 2): return False
    if tile_num % glen:  # from 2nd col check that tile's right edge matches previous col's left edge
        if edge(tile_num, orientation, 1) != edge(tile_pos - 1, orientation, 3): return False
    return True


def solve_grid(start_pos):
    for tile in range(start_pos, len(tiles)):
        print(ok_tile(start_pos, tile, 0))
    # if not ok_tile(): return False
    # if len(available) == 0: return True
    # try_tile = available.pop()
    # print('try_tile', try_tile)
    # for loc_orientation in range(8):
    #     # ... grid.append((try_tile, loc_orientation))
    #     if solve_grid(available):
    #         print('YES')
    #     else:
    #         print('NO')
    return True


if __name__ == '__main__':
    with open('d20.in1', 'r') as f:
        content = f.read()
    rec = content.split('\n\n')
    tiles = {int(x.split(':')[0][5:]): x.split('\n')[1:11] for x in rec}
    tile_len = 10
    glen = int(sqrt(len(tiles)))  # grid side length
    grid = [(2311, 1)] * len(tiles)

    solve_grid(4)

    for one_tile in tiles.keys():
        for oriented in range(4):
            # print(edge(tile, orientation), tile, orientation)
            edges[edge(one_tile, 0, oriented)].append((one_tile, oriented))
            edges[edge(one_tile, 1, oriented)].append((one_tile, oriented))

    for one_tile in tiles.keys():
        fit = 0
        for oriented in range(4):
            fit += int(len(edges[edge(one_tile, 0, oriented)]) / 2)
            fit += int(len(edges[edge(one_tile, 1, oriented)]) / 2)
        print(one_tile, fit)
    
    # orientations = list([range(4)] * glen * glen)
    # a = 0
    # for perm in zip(product(permutations(tiles.keys()), product(*orientations))):
    #     a += 1
