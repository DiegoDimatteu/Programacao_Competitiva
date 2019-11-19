import math
a = int(input())
b = [int(i) for i in input().split()]
um = 0
dois = 0
tres = 0
count = a
condicion = 0
car = 0
 
for i in b:
	if i == 3:
		tres += 1
	elif i == 1:
		um +=1 
	elif i == 2:
		dois += 1
 
while tres > 0 and um > 0:
		tres -= 1
		um -= 1
		count -= 1
 
while dois > 0 and um > 0:
	if condicion == 0:
		car = 1
	condicion += 1
	um -= 1
	count -= 1
	if condicion == 2:
		condicion = 0
		dois -= car
		car = 0
 
dois -= car
		
while dois > 1:
	dois -= 2
	count -= 1
 
condicion = 0
car = 0
 
while um > 0:
	if condicion == 0:
		car +=1
	um -= 1
	count -= 1
	condicion += 1
	if condicion == 4:
		condicion = 0
 
count += car
 
print(count)