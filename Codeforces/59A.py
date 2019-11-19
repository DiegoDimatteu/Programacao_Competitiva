a = input()
countM = 0
countm = 0
for i in range (len(a)):
	if a[i].islower():
		countm += 1
	else:
		countM += 1
if countm >= countM:
	print(a.lower())
else:
	print(a.upper())