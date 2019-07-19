bala=int(input())
li=[]
for i in range(bala):
    for j in range(i,bala):
        li.append("1")
    print(*li)
    li=[]
