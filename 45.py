bala,k=input().split()
bala==str(bala)
k=int(k)
for i in range (0,len(bala)):
  if len(bala[i:i+k])==k:
    print(bala[i:i+k],end=" ")
