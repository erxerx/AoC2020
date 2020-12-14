def howmanywithinside(bag):
  if rules[bag] == ['no other']: return 1
  sum = 0
  for i in rules[bag]:
    cnt=int(i[:i.index(' ')])
    kind=i[i.index(' ') + 1:]
    sum += cnt * howmanywithinside(kind)

def many_contain(color):
  contains = {color}
  num=0
  while num < len(contains):
    num = len(contains)
    for i in ll:
      for col in contains:
        if col == i[0]:
          contains.add(i[1])
          break
  return len(contains)

with open('d07.in', 'r') as f:
  content = f.read()
l = content.split('\n')
ll = [x.replace('\n', '').split(' contain ') for x in l]
#rules = [[i[0], i[1].split(', ')] for i in ll]
rules = {i[0]:i[1].split(', ') for i in ll}
#rule = [ i[0], [ x.lstrip(' ')[:x.index(' ')], x[x.index(' ') + 1::] for x in i[1].split(',') ] for i in ll ]
#rules = [[[line[0], [x.lstrip(' ')[:x.index(' '):], x.lstrip(' ')[x.index(' ') + 1::]]] for x in line[1].split(',')] for line in ll]
print(howmanywithinside('shiny gold'))

#print(many_contain('shiny gold bag'))
