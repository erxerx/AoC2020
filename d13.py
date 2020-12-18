#intervals = [7,13,0,0,59,0,31,19]
intervals = [17,0,0,0,0,0,0,0,0,0,0,37,0,0,0,0,0,439,0,29,0,0,0,0,0,0,0,0,0,0,13,0,0,0,0,0,0,0,0,0,23,0,0,0,0,0,0,0,787,0,0,0,0,0,0,0,0,0,41,0,0,0,0,0,0,0,0,19]
n=[]
a=[]
for i in range(len(intervals)):
    if intervals[i] == 0: continue
    n.append(intervals[i])
    a.append(i)
print(n,a)
