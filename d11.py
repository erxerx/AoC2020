with open('d11.in', 'r') as f:
  content = f.read()
l = ['.' + x + '.' for x in content.split('\n')]
lenn=len(l[0])
l = ['.' * lenn] + l + ['.' * lenn]
n=l[::]
l[0]=['A' * lenn]
while l != n:
  l = n[::]
  occupied = 0
  for y in range(1,len(l)):
    for x in range(1,lenn):
      #around = ''.join([i[x-1:x+2] for i in l[y-1:y+2]]).count('#') - l[y][x].count('#')
      around = 0
      for dy in [-1,0,1]:
        for dx in [-1, 0, 1]:
          if dx == 0 and dy == 0: continue
          #print('dxy',dy,dx)
          for i in range(1,lenn):
            nx = i * dx + x
            ny = i * dy + y
            if nx == 0 or nx == lenn: break
            if ny == 0 or ny == len(l): break
            if l[ny][nx] == 'L': break
            if l[ny][nx] == '#': around += 1; break
      if l[y][x] == 'L' and around == 0: n[y] = n[y][:x] + '#' + n[y][x+1:]; occupied += 1
      if l[y][x] == '#' and around >  4: n[y] = n[y][:x] + 'L' + n[y][x + 1:]
  print(''.join(n).count('#'), n)
