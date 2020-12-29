def howmanywithinside(bag):
    if rules[bag] == ['no other']: return 1
    sum = 0
    for i in rules[bag]:
        cnt = int(i[:i.index(' ')])
        kind = i[i.index(' ') + 1:]
        sum += cnt * howmanywithinside(kind)


def many_contain(color):
    contains = {color}
    num = 0
    while num < len(contains):
        num = len(contains)
        for i in ll:
            for col in contains:
                if col == i[0]:
                    contains.add(i[1])
                    break
    return len(contains)


def solve_contains(start_pos):
  # check if all foods that contain allergen a contain also ingredient i
  for food in foods:
    ingredients.update(food[0].split(' '))
    allergens.update(food[1].split(', '))
    for allergen in allergens:
        if allergen in a2i: continue
        for ingredient in ingredients:
          if ingredient in i2a: continue
          i2a[ingredient] = allergen
          a2i[allergen] = ingredient
          if solve_contains(start_pos + 1): return True
        for ingredient in ingredients:
            print(ingredient)
    #     if not ok_tile(start_pos, tile, orientation): continue  # does not fit, take next
    #     grid_tiles[start_pos] = tile
    #     grid_orientations[start_pos] = orientation  # let's try it out
    #     print('at', start_pos, 'trying', tile, orientation)
    #     if start_pos == len(tiles) - 1: return True  # solution found if all in place
    #     if solve_grid(start_pos + 1): return True
    # grid_tiles[start_pos] = 0
    return False  # dead end, backtrack


with open('d21.in1', 'r') as f:
    content = f.read()
l = content.split('\n')
foods = [x.replace('\n', '').split(' (contains ') for x in l]
ingredients = set('')
allergens = set('')
i2a = {}
a2i = {}
contains = {}
# let's populate these by processing foods :)
for food in foods:
    # print(food)
    ingredients.update(food[0].split(' '))
    allergens.update(food[1].split(', '))
print(ingredients, '\n', allergens)
print(solve_contains(0))

# rules = [[i[0], i[1].split(', ')] for i in ll]
# rules = {i[0]:i[1].split(', ') for i in ll}
# rule = [ i[0], [ x.lstrip(' ')[:x.index(' ')], x[x.index(' ') + 1::] for x in i[1].split(',') ] for i in ll ]
# rules = [[[line[0], [x.lstrip(' ')[:x.index(' '):], x.lstrip(' ')[x.index(' ') + 1::]]] for x in line[1].split(',')] for line in ll]
# print(howmanywithinside('shiny gold'))

# print(many_contain('shiny gold bag'))
