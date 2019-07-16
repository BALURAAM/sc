N=int(input())
p=str(N)
a=len(p)
su=0
res=1
for i in range(0,a):
    rem=N%10
    res=rem**a
    su=su+(res)
    N=N//10
print(su)
