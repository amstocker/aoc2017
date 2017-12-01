with open('input.txt') as f:
  inpt = f.read().rstrip()

l = len(inpt)
print(l)

s = 0
for i in range(l):
  cur = inpt[i]
  nxt = inpt[(i+1)%l]
  if cur == nxt:
    s += int(cur)
print("part1: {}".format(s))

s = 0
for i in range(l):
  cur = inpt[i]
  nxt = inpt[(i+l//2)%l]
  if cur == nxt:
    s += int(cur)
print("part2: {}".format(s))
