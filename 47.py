import math
bala, b = list(map(int,input().split()))
if bala <= 100:
  bala = math.factorial(bala)
else:
  bala = 0
if b <= 100:
  b = math.factorial(b)
else:
  b = 0
while bala != 0 and b != 0:
  if bala > b:
    bala -= b
  else:
    b -= bala
if bala == 0:
  print(b)
else:
  print(b)
