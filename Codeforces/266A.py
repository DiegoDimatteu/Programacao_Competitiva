a = int(input())
b = input()
c = len(b)
i = 0
 
while i < len(b):
	if i == len(b) - 1:
		pass
	elif b[i] == b[i + 1]:
		c -= 1
	i += 1
print(len(b) - c)