with open('input.txt') as f:
  inpt = f.read()

lines = inpt.split('\n')[:-1]

valid = 0
for line in lines:
  words = line.split()
  tmp = set()
  for word in words:
    if word in tmp:
      break
    else:
      tmp.add(word)
  else:
    valid += 1

print(valid)


from collections import defaultdict
def lc(word):
  d = defaultdict(int)
  for c in word:
    d[c] += 1
  return d

def check_line(words):
  lcs = []
  for word in words:
    count = lc(word)
    for c in lcs:
      if count == c:
        return False
    lcs.append(count)
  return True

valid = 0
for line in lines:
  if check_line(line.split()):
    valid += 1
  
print(valid)
