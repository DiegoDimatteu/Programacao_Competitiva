import math
a, b = [int(i) for i in input().split()]
count = 1
if (math.ceil(a / 2)) >= b:
	print((b * 2) - 1)
else:
	b -= math.ceil(a/2)
	print(b * 2)