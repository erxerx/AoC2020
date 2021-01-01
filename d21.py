def solve_contains(a, i):
    # check if all foods that contain allergen a contain also ingredient i
    if a:
        for food in foods:
            if a in food[1].split(', ') and not i in food[0].split(' '):
                return False
    i2a[i] = a
    a2i[a] = i
    if len(a2i) == len(allergens) + 1: return True
    for allergen in allergens:
        if allergen in a2i: continue
        for ingredient in ingredients:
            if ingredient in i2a: continue
            if solve_contains(allergen, ingredient): return True
    i2a.pop(a2i[allergen])
    a2i.pop(allergen)
    return False  # dead end, backtrack


with open('d21.in', 'r') as f:
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
    ingredients.update(food[0].split(' '))
    allergens.update(food[1].split(', '))
print(ingredients, '\n', allergens)
print(solve_contains('',''))
nonallergenic = 0
for food in foods:
    for i in food[0].split(' '):
        if not i in i2a: nonallergenic += 1
#part1
print(nonallergenic)
print(a2i)
print(sorted(a2i))
#part2: dhfng,pgblcd,xhkdc,ghlzj,dstct,nqbnmzx,ntggc,znrzgs
