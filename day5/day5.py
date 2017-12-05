with open('input.txt') as f:
  _lines = [int(line.rstrip()) for line in f.read().rstrip().split('\n')]

lines = [x for x in _lines]
count = 0
cur = 0
size = len(lines)
while cur < size:
  step = lines[cur]
  lines[cur] += 1
  cur += step
  count += 1

print(count)


lines = [x for x in _lines]
count = 0
cur = 0
size = len(lines)
while cur < size:
  step = lines[cur]
  if step < 3:
    lines[cur] += 1
  else:
    lines[cur] -= 1
  cur += step
  count += 1

print(count)
