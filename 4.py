def PS(a, b): 

	count = 0  
	for i in range (a, b + 1): 
		j = 1; 
		while j * j <= i: 
			if j * j == i: 
				count = count + 1
			j = j + 1
		i = i + 1
	return count


a = int(input())
b = int(input())
print (PS(a, b)) 
