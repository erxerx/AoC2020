with open('/home/ervin/AdventOfCode2020/d01_1.in', 'r') as f:
  d=f.readlines()
  for i in d:
    for j in d:
      for k in d:
        if int(i) + int(j) + int(k) == 2020:
          print(int(i)*int(j)*int(k))
