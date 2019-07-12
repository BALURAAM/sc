import math 
def PS(a, b): 
	return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1) 
a = int(input())
b = int(input())
print (int(PS(a, b))) 
