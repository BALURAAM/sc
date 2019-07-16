bala=input()
ram=input()
a=[]
b=[]
c=[]
for i in bala:
    a.append(ord(i)-ord('a'))
for i in ram:
    b.append(ord(i)-ord('a'))
for i,j in zip(a,b):
    c.append((chr((i+j)%26+ord('a')+1)))
print("".join(c))
