from collections import defaultdict
from itertools import product
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
    if tile_pos >= glen:  # from 2nd row check that tile's upper edge matches previous row's lower edge
        if edge(tile_num, orientation, 0) != edge(*grid[tile_pos - glen], 2): return False
    if tile_pos % glen:  # from 2nd col check that tile's left edge matches previous col's right edge
        if edge(tile_num, orientation, 3) != edge(*grid[tile_pos - 1], 1): return False
    return True


def solve_grid(start_pos):
    for tile, orientation in available:
        print('at', start_pos, 'trying', tile, orientation)
        if not ok_tile(start_pos, tile, orientation): continue  # does not fit, take next
        grid[start_pos] = (tile, orientation)  # let's try it out
        available.remove((tile, 0))  # remove used one from available list and continue search
        available.remove((tile, 1))  # remove all orientations
        if start_pos == len(tiles): return True  # solution found if all in place
        if solve_grid(start_pos + 1):
            return True
        else:
            available.add((tile, 0))  # if can not use, add back to available set
            available.add((tile, 1))  # if can not use, add back to available set
    grid[start_pos] = (0, 0)
    return False  # dead end, backtrack

    # if not available: return False  # dead end
    # elif tile_pos < glen:  # set of tiles and orientations that match prev tile's right edge
    #     available = [x for x in edges[edge(*grid[tile_pos - 1], 1)]]
    # if
    #
    # print('available:', len(list(available)))
    # # print(ok_tile(tile_pos, 1427, 0))
    # [ x for x in edges['###.##.#..'] if x[2] == 2 ]
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
    # return True


if __name__ == '__main__':
    with open('d20.in1', 'r') as f:
        content = f.read()
    rec = content.split('\n\n')
    tiles = {int(x.split(':')[0][5:]): x.split('\n')[1:11] for x in rec}
    tile_len = 10
    glen = int(sqrt(len(tiles)))  # grid side length
    grid = [(0, 0)] * len(tiles)

    for one_tile in tiles.keys():
        for enum in range(4):
            # print(edge(tile, orientation), tile, orientation)
            edges[edge(one_tile, 0, enum)].append((one_tile, 0, enum))
            edges[edge(one_tile, 1, enum)].append((one_tile, 1, enum))

    for one_tile in tiles.keys():
        fit = 0
        for enum in range(4):
            fit += int(len(edges[edge(one_tile, 0, enum)]) / 2)
            fit += int(len(edges[edge(one_tile, 1, enum)]) / 2)
        # print(one_tile, fit)

    available = set(product(tiles.keys(), [0, 1]))  # all tiles and orientations could match
    print(solve_grid(0))

    # orientations = list([range(4)] * glen * glen)
    # a = 0
    # for perm in zip(product(permutations(tiles.keys()), product(*orientations))):
    #     a += 1
