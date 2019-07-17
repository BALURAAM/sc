k = input()
x = input().split()
p = input()
l = len(p)
bala = 0
for i in x:
    if i[:l] == p:
        bala += 1
print(bala)
