a, b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
count = 0
for i in range (len(c)):
	if c[i] > b:
		count += 2
	else:
		count += 1
print(count)