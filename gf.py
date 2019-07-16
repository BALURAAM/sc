n = int(input())
bala = 0
for i in range(n):
  if 2**i == n:
    bala = 1
    break
if bala == 1:
  print("yes")
else:
  print("no")
