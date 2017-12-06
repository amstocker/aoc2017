with open('input.txt') as f:
  _banks = [int(v) for v in f.read().rstrip().split()]
  N = len(_banks)

def redist(banks):
  banks = list(banks)
  max_val = max(banks)
  max_idx = banks.index(max_val)
  banks[max_idx] = 0
  
  cur = (max_idx + 1) % N
  while max_val > 0:
    banks[cur] += 1
    cur = (cur + 1) % N
    max_val -= 1

  return tuple(banks)

count = 0
banks = tuple(_banks)
configs = {banks: count}
while True:
  banks = redist(banks)
  count += 1
  if banks in configs:
    break
  else:
    configs[banks] = count

print("{} after {} iters".format(count, (count - configs[banks])))
