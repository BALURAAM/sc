def bala(a,b): 
	if(b==0): 
		return a 
	else: 
		return bala(b,a%b) 

a = int(input())
b= int(input())
print (bala(a,b)) 
