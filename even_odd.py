list1 = [5,8,9,12,15]

even, odd = 0, 0
for num in list1:
	
	if num % 2 == 0:
		even += 1

	else:
		odd += 1
		
print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)
