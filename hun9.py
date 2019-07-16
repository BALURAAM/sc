bala=list(input())
c=0
bala=list(map(int,bala))
for i in bala:
    if i%2!=0:
        c=c+i
if c%2==0:
    print('E')
else:
    print('O')
