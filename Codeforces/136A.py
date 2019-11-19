a = int(input())
b = [int(i) for i in input().split()]
c = [0 for i in range (a)]
for i in range (a):
	d = b[i]
	c.insert(d, i + 1)
	del(c[d - 1])
for i in range (a):
	print(c[i] , end = '')
	print(' ', end = '')