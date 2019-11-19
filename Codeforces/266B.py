a, b = [int(i) for i in input().split()]
s = list(input())
count = 0
i = 0
while count < b:
	i = 0
	while i < len(s) - 1:
		if s[i+1] == 'G' and s[i] == 'B':
			s[i] = 'G'
			s[i + 1] = 'B'
			i += 2
		else:
			i += 1
	count += 1
 
print(*s, sep = '')