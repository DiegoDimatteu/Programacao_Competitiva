a,b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
c.sort()
menor = 1000
i = a - 1
while i < b:
	if (c[i] - c[(i - a) + 1]) < menor:
		menor = c[i] - c[(i - a) + 1]
	i += 1
print(menor)