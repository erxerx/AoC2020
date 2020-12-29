if __name__ == '__main__':
    with open('d20.out', 'r') as f:
        content = f.read()
    tiles = content.split('\n')

    tile_len = len(tiles)
    glen = 1  # grid side length
    im = ['.' * tile_len] * tile_len

    # search whole image all rotations for sea-monster
    monsters = 0
    for orientation in range(8):
        for y in range(tile_len):
            n = tiles[y]
            e = ''.join(tiles[yy][tile_len-y-1] for yy in range(tile_len))
            s = tiles[tile_len-y-1]
            w = ''.join(tiles[yy][y] for yy in range(tile_len))
            if orientation == 0:   res = n
            elif orientation == 1: res = w[::-1]
            elif orientation == 2: res = s[::-1]
            elif orientation == 3: res = e
            elif orientation == 4: res = n[::-1]
            elif orientation == 5: res = e[::-1]
            elif orientation == 6: res = s
            else: res = w
            im[y] = res
        print('\nOrientation', orientation)
        # for line in im:
        #     print(line)
        for y in range(tile_len-2):
            for x in range(tile_len-21):
                lookat = im[y][x + 18] + im[y + 1][x] + im[y + 1][x + 5:x + 7] + im[y + 1][x + 11:x + 13] + \
                    im[y + 1][x + 17:x + 20] + im[y + 2][x + 1] + im[y + 2][x + 4] + im[y + 2][x + 7] + \
                    im[y + 2][x + 10] + im[y + 2][x + 13] + im[y + 2][x + 16]
                if lookat == '#' * 15:
                    print('Found monster at', x, y)
                    monsters += 1

    print('Total monsters', monsters)
    print('Number of non-monster blocks', ''.join(tiles).count('#') - 15 * monsters)
