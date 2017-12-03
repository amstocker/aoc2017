N = 289326

cur = (0,0)
direc = 0     # 0=R, 1=U, 2=L, 3=D
ln = 1
tick = 0
vals = {cur: 1}
trackingVals = True

def nbr(x, y):
  return (cur[0] + x, cur[1] + y)

for i in range(N):
  if i == N-1:
    print(abs(cur[0]) + abs(cur[1]))
  if tick == 2*ln:
    tick = 0
    ln += 1
    direc  = (direc + 1) % 4
  elif tick == ln:
    direc  = (direc + 1) % 4
  if direc == 0:
    cur = (cur[0] + 1, cur[1])
  elif direc == 1:
    cur = (cur[0], cur[1] + 1)
  elif direc == 2:
    cur = (cur[0] - 1, cur[1])
  elif direc == 3:
    cur = (cur[0], cur[1] - 1)
  tick += 1
  if trackingVals:
    val = 0
    if nbr(1, 0) in vals:
      val += vals[nbr(1, 0)]
    if nbr(1, 1) in vals:
      val += vals[nbr(1, 1)]
    if nbr(0, 1) in vals:
      val += vals[nbr(0, 1)]
    if nbr(-1, 1) in vals:
      val += vals[nbr(-1, 1)]
    if nbr(-1, 0) in vals:
      val += vals[nbr(-1, 0)]
    if nbr(-1, -1) in vals:
      val += vals[nbr(-1, -1)]
    if nbr(0, -1) in vals:
      val += vals[nbr(0, -1)]
    if nbr(1, -1) in vals:
      val += vals[nbr(1, -1)]
    vals[cur] = val
    if val > N:
      print(val)
      trackingVals = False
