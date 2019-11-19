a = int(input())
count = 0
for i in range (a):
	b,c = [int(i) for i in input().split()]
	d = c - b
	if d >= 2:
		count += 1
 
print(count)