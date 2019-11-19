a = int(input())
i = 0
xs = 0
ys = 0
zs = 0
 
while i < a:
	x,y,z = [int(j) for j in input().split()]
	xs += x
	ys += y
	zs += z
	i += 1
if xs == 0 and ys == 0 and zs == 0:
	print('YES')
else:
	print('NO')