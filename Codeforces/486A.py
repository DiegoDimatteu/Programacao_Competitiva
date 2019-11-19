import math
a = int(input())
if a % 2 == 0:
	a /= 2
	print("%.0f"%a)
else:
	print((-1) * (math.ceil(a/2)))