bala = int(input())
ram = list(map(int,input().split()))
c = sorted(ram)
d = c[::-1]
e = []
for i in range(0,len(ram)):
  e.append(d[i])
  e.append(c[i])
for j in e[:len(ram)]:
  print(j,end = " ")
