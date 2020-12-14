from re import search
with open('d04.in', 'r') as f:
  content = f.read()
l = content.split('\n\n')
ll = [x.replace('\n', ' ').split(' ') for x in l]
c = 0
tt= []
for i in ll:
  id = { 'cid' : 'def'}
  id.update({ii[:ii.index(':')]:ii[ii.index(':') + 1::] for ii in i})
  if len(id) != 8: continue
  if not search('cm|in',id['hgt']): continue
  if search('cm',id['hgt']) and (int(id['hgt'].rstrip('cm')) < 150 or int(id['hgt'].rstrip('cm')) > 193):
    continue
  if search('in',id['hgt']) and (int(id['hgt'].rstrip('in')) < 59 or int(id['hgt'].rstrip('in')) > 76):
    continue
  if not search('#[0-9a-f]{6}',id['hcl']): continue
  if int(id['byr']) < 1920 or int(id['byr']) > 2002:
    continue
  if int(id['iyr']) < 2010 or int(id['iyr']) > 2020:
    continue
  if int(id['eyr']) < 2020 or int(id['eyr']) > 2030:
    continue
  if not search(id['ecl'],'amb,  blu,  brn,  gry,  grn,  hzl,  oth'):
    continue
  if not search('^[0-9]{9}$', id['pid']):
    continue
  c += 1
  for key in sorted(id):
    print("%s: %s\t" % (key, id[key]), end = ' ')
  print('\n')
print(c)
