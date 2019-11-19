a = []
for j in range(5):
	a.append([int (i) for i in input().split()])
k = [(i, a.index(1)) for i, a in enumerate(a) if 1 in a]
i,j = k[0]
 
count = abs(2 - i) + abs(2 - j)
 
print(count)