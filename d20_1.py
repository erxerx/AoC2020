from math import sqrt


def edge(tile_num, orientation, edge_num):  # return tile edge
    n = tiles[tile_num][0]
    e = ''.join([tiles[tile_num][x][tile_len - 1] for x in range(tile_len)])
    s = tiles[tile_num][tile_len - 1]
    w = ''.join([tiles[tile_num][x][0] for x in range(tile_len)])
    if orientation == 0:
        if edge_num == 0: return n
        if edge_num == 1: return e
        if edge_num == 2: return s
        if edge_num == 3: return w
    elif orientation == 1:
        if edge_num == 0: return w[::-1]
        if edge_num == 1: return n
        if edge_num == 2: return e[::-1]
        if edge_num == 3: return s
    elif orientation == 2:
        if edge_num == 0: return s[::-1]
        if edge_num == 1: return w[::-1]
        if edge_num == 2: return n[::-1]
        if edge_num == 3: return e[::-1]
    elif orientation == 3:
        if edge_num == 0: return e
        if edge_num == 1: return s[::-1]
        if edge_num == 2: return w
        if edge_num == 3: return n[::-1]
    elif orientation == 4:
        if edge_num == 0: return n[::-1]
        if edge_num == 1: return w
        if edge_num == 2: return s[::-1]
        if edge_num == 3: return e
    elif orientation == 5:
        if edge_num == 0: return e[::-1]
        if edge_num == 1: return n[::-1]
        if edge_num == 2: return w[::-1]
        if edge_num == 3: return s[::-1]
    elif orientation == 6:
        if edge_num == 0: return s
        if edge_num == 1: return e[::-1]
        if edge_num == 2: return n
        if edge_num == 3: return w[::-1]
    elif orientation == 7:
        if edge_num == 0: return w
        if edge_num == 1: return s
        if edge_num == 2: return e
        if edge_num == 3: return n


def ok_tile(tile_pos, tile_num, orientation):
    if tile_pos >= glen:  # from 2nd row check that tile's upper edge matches previous row's lower edge
        if edge(tile_num, orientation, 0) != edge(grid_tiles[tile_pos - glen], grid_orientations[tile_pos - glen], 2):
            return False
    if tile_pos % glen:  # from 2nd col check that tile's left edge matches previous col's right edge
        if edge(tile_num, orientation, 3) != edge(grid_tiles[tile_pos - 1], grid_orientations[tile_pos - 1], 1):
            return False
    return True


def solve_grid(start_pos):
    for tile in tiles.keys():
        if tile in grid_tiles: continue
        for orientation in range(8):
            if not ok_tile(start_pos, tile, orientation): continue  # does not fit, take next
            grid_tiles[start_pos] = tile
            grid_orientations[start_pos] = orientation  # let's try it out
            print('at', start_pos, 'trying', tile, orientation)
            if start_pos == len(tiles) - 1: return True  # solution found if all in place
            if solve_grid(start_pos + 1): return True
    grid_tiles[start_pos] = 0
    return False  # dead end, backtrack


if __name__ == '__main__':
    with open('d20.in', 'r') as f:
        content = f.read()
    rec = content.split('\n\n')
    tiles = {int(x.split(':')[0][5:]): x.split('\n')[1:11] for x in rec}
    values_view = tiles.values()
    value_iterator = iter(values_view)
    first_value = next(value_iterator)
    tile_len = len(first_value)
    glen = int(sqrt(len(tiles)))  # grid side length
    grid_tiles = [0] * len(tiles)
    grid_orientations = [0] * len(tiles)
    print(solve_grid(0))
    print(grid_tiles[0] * grid_tiles[glen - 1] * grid_tiles[len(tiles) - glen] * grid_tiles[len(tiles) - 1])
