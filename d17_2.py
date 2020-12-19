import numpy as np
initial = [[0,0,1,1,0,1,0,1],
[1,1,0,0,0,0,1,0],
[0,0,0,0,1,1,1,1],
[1,0,0,1,1,0,0,0],
[1,0,0,1,0,1,1,0],
[0,1,0,0,1,0,0,0],
[1,1,0,0,0,1,1,0],
[0,1,0,0,0,1,0,0]]
steps = 6
rad = steps + 4
lenn = 2* rad
state     = np.zeros((lenn,lenn,lenn,lenn), dtype=np.uint8)
#state[rad][rad][rad - 1][rad] = 1
#state[rad][rad][rad][rad + 1] = 1
#state[rad][rad][rad + 1][rad - 1] = 1
#state[rad][rad][rad + 1][rad] = 1
#state[rad][rad][rad + 1][rad + 1] = 1
for y in range(len(initial)):
  state[rad][rad][rad - 4 + y][rad - 4: rad + 4] = initial[y]
for step in range(1,steps + 1):
  nextstate = np.zeros((lenn, lenn, lenn,lenn), dtype=np.uint8)
  print('step:', step)
  alive = 0
  for w in range(rad - step - 0, rad + step + 1):
    #print('w:',w)
    for z in range(rad - step - 3, rad + step + 3):
      #print('z:',z)
      for y in range(rad - step - 3, rad + step + 3):
        #print('y:', y)
        for x in range(rad - step - 3, rad + step + 3):
          #print('x:', x)
          around = 0
          for dw in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
              for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                  if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                    continue
                  ix, iy, iz, iw = x + dx, y + dy, z + dz, w + dw
                  if (ix < 0 or ix > lenn - 1) or (iy < 0 or iy > lenn - 1) or (iz < 0 or iz > lenn - 1) or (iw < 0 or iw > lenn - 1): continue
                  around += state[iw][iz][iy][ix]
                  #print('xyzw:',x,y,z,w, 'ixiyiziw:',ix,iy,iz,iw)
            #print('around:',around)
          if around == 3:
            #print(x,y,z,w,' will become alive 1 !')
            alive += 1
            nextstate[w][z][y][x] = 1
          elif around == 2 and state[w][z][y][x] == 1:
            #print(x,y,z,w,' will become alive  2!')
            alive += 1
            nextstate[w][z][y][x] = 1
  #        else:
  #          nextstate[z][y][x] = 0
  print('alive:', alive)
  state = nextstate[::]
