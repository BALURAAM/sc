t=input()
bala=[]
for i in range(0,len(t)-1):
    if t[i]==t[i+1]:
        x=t[:i+1]+t[i+2:]
        bala.append(x)
bala.sort()
print(bala[-1])
#225634486
#25634486
