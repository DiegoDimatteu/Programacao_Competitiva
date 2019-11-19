a = input()
i = 0
b = []
while i < len(a):
	if a[i] == 'a' or a[i] == 'A' or a[i] == 'o' or a[i] == 'O' or a[i] == 'y' or a[i] == 'Y' or a[i] == 'e' or a[i] == 'E' or a[i] == 'u' or a[i] == 'U' or a[i] == 'i' or a[i] == 'I':
		pass
	elif a[i].isupper():
		b.append('.' + a[i].lower())
	elif a[i].islower():
		b.append('.' + a[i])
	i += 1
for j in range (len(b)):
	if j == len(b) - 1:
		print(b[j])
	else:
		print(b[j], end = '')