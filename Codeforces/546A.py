k, n, w = [int(i) for i in input().split()]
multiplier = 1
value = 0
for i in range (w):
	value += k * multiplier
	multiplier += 1
if value > n:
	print(value - n)
else:
	print('0')
