
def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf
a, b = list(map(int,input().split()))
num1=1
for i in range(1,a+1):
    num1=num1*i
num2=1
for i in range(1,b+1):
    num2=num2*i
print(computeHCF(num1, num2))
