def solve_contains(a, i):
    # check if all foods that contain allergen a contain also ingredient i
    if a:
        for food in foods:
            if a in food[1].split(', ') and not i in food[0].split(' '):
                    return False
    for allergen in allergens:
        if allergen in a2i: continue
        for ingredient in ingredients:
            if ingredient in i2a: continue
            i2a[ingredient] = allergen
            a2i[allergen] = ingredient
            if len(a2i) == len(allergens): return True
            if solve_contains(start_pos + 1): return True
            i2a.pop(a2i[allergen])
            a2i.pop(allergen)
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
print(solve_contains('',''))
print(a2i)
# rules = [[i[0], i[1].split(', ')] for i in ll]
# rules = {i[0]:i[1].split(', ') for i in ll}
# rule = [ i[0], [ x.lstrip(' ')[:x.index(' ')], x[x.index(' ') + 1::] for x in i[1].split(',') ] for i in ll ]
# rules = [[[line[0], [x.lstrip(' ')[:x.index(' '):], x.lstrip(' ')[x.index(' ') + 1::]]] for x in line[1].split(',')] for line in ll]
# print(howmanywithinside('shiny gold'))

# print(many_contain('shiny gold bag'))
