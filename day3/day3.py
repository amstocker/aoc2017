Cur = (0,0)
Dir = 0
Len = 1
Tick = 0
# 0=R, 1=U, 2=L, 3=D
for i in range(289326):
  if i == 289325:
    print(abs(Cur[0]) + abs(Cur[1]))
  if Tick == 2*Len:
    Tick = 0
    Len += 1
    Dir  = (Dir + 1) % 4
  elif Tick == Len:
    Dir  = (Dir + 1) % 4
  if Dir == 0:
    Cur = (Cur[0] + 1, Cur[1])
  elif Dir == 1:
    Cur = (Cur[0], Cur[1] + 1)
  elif Dir == 2:
    Cur = (Cur[0] - 1, Cur[1])
  elif Dir == 3:
    Cur = (Cur[0], Cur[1] - 1)
  Tick += 1
