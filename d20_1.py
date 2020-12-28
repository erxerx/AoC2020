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
    with open('d20.in1', 'r') as f:
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
    # grid_tiles = [
    #     1831, 3607, 2677, 3449, 1451, 1013, 2953, 2999, 2731, 3583, 3529, 1699, 1423, 3671, 3461, 2971, 3023, 1249,
    #     2687, 3539, 3313, 2593, 3329, 2251, 1069, 2179, 2903, 2621, 2549, 2083, 3209, 1697, 1657, 2963, 1499, 1367,
    #     1877, 1973, 3001, 3673, 2897, 3221, 2081, 1693, 2927, 2437, 2939, 3767, 1871, 3467, 2887, 1433, 3343, 3697,
    #     3413, 1511, 2129, 1951, 2339, 2693, 3989, 2423, 3931, 1453, 2917, 1949, 3331, 3433, 3911, 1307, 2267, 3929,
    #     3851, 2053, 3217, 3797, 2089, 3259, 1759, 2341, 3011, 1153, 1123, 2441, 2087, 3517, 2297, 1087, 2221, 1481,
    #     1459, 1471, 2237, 2281, 2357, 2017, 1747, 2069, 3041, 3769, 3643, 2459, 2467, 1103, 1279, 2203, 1847, 2011,
    #     2663, 1171, 1303, 3631, 2311, 3079, 3533, 3919, 1151, 2389, 1789, 1667, 2633, 1597, 1487, 3547, 3943, 3581,
    #     1039, 1907, 1109, 2671, 3557, 1559, 2789, 1549, 2381, 3617, 2729, 2647, 2797, 2417, 2029, 2767, 3391, 2309]
    # grid_orientations = [
    #     2, 0, 3, 5, 4, 0, 2, 5, 5, 0, 0, 3, 3, 0, 6, 2, 6, 0, 3, 6, 6, 5, 3, 5, 4, 5, 5, 2, 5, 3, 5, 2, 4, 5, 5, 6, 0,
    #     4, 4, 0, 6, 2, 5, 0, 3, 5, 0, 1, 3, 4, 2, 6, 0, 3, 2, 5, 5, 1, 5, 0, 6, 5, 5, 2, 6, 1, 3, 6, 3, 5, 2, 3, 3, 2,
    #     6, 6, 0, 0, 3, 0, 3, 5, 2, 1, 3, 6, 6, 0, 1, 1, 2, 3, 2, 5, 4, 2, 4, 6, 3, 6, 6, 2, 4, 4, 2, 5, 4, 1, 5, 5, 1,
    #     2, 3, 4, 4, 2, 1, 5, 0, 1, 0, 3, 6, 2, 6, 2, 0, 5, 5, 4, 3, 0, 6, 3, 3, 5, 5, 0, 5, 5, 1, 3, 2, 3]
    image = ['.' * (tile_len - 2)*glen] * (tile_len - 2)*glen
    print(grid_tiles)
    print(grid_orientations)
    print(grid_tiles[0] * grid_tiles[glen - 1] * grid_tiles[len(tiles) - glen] * grid_tiles[len(tiles) - 1])
    xx = 0; yy = 0
    for tile_num in range(len(tiles)):
        for y in range(tile_len - 2):
            # for x in range(tile_len - 2):
            n = tiles[grid_tiles[tile_num]][y + 1][1:tile_len - 1]
            e = ''.join(tiles[grid_tiles[tile_num]][yy][tile_len - y - 2] for yy in range(1, tile_len - 1))
            s = tiles[grid_tiles[tile_num]][tile_len - y - 2][1:tile_len - 1]
            w = ''.join(tiles[grid_tiles[tile_num]][yy][y + 1] for yy in range(1, tile_len - 1))
            orientation = grid_orientations[tile_num]
            if orientation == 0:   res = n
            elif orientation == 1: res = w[::-1]
            elif orientation == 2: res = s[::-1]
            elif orientation == 3: res = e
            elif orientation == 4: res = n[::-1]
            elif orientation == 5: res = e[::-1]
            elif orientation == 6: res = s
            elif orientation == 7: res = w
            # print(y, res)
            image[yy+y] = image[yy+y][:xx] + res + image[yy+y][xx+tile_len-2:]
        xx += tile_len-2
        if xx == (tile_len-2)*glen:
            xx = 0
            yy += tile_len-2
    print(image)