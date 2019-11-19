a = int(input())
i = 0
count = 0
while i < a:
	p, v, t = [int (i) for i in input().split()]
	if (p + v + t) > 1:
		count += 1
	i += 1
print(count)