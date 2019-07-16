N=int(input())
p=str(N)
a=len(p)
sum=0
for i in range(0,N):
    rem=N%10
    sum=sum+(rem*a)
    N/=10
print(sum)
