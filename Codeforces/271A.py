a = int(input())
count = 0
a += 1
while count == 0:
	b = a
	u = b % 10
	b -= u
	d = b % 100
	b -= d
	d /= 10
	c = b % 1000
	b -= c
	c /= 100
	m = b % 10000
	m /= 1000
	if u != d and u != c and u != m and d != c and d != m and c != m:
		count = 1
	else:
		a += 1
 
print(a)