n=int(input())
bala=[]
for i in range(n):
  v=input()
  bala.append(v)
mval=min(bala,key=len)
bala.remove(mval)
for i in range(len(mval)):
  for j in range(len(bala)):
     cval=bala[j]
     if mval[:i+1]==cval[:i+1]:
       result=mval[:i+1]
     else:
       break
print(result)
