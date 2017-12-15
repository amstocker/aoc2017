a = 699
b = 124

def a_update(n):
  return (n * 16807) % 2147483647

def b_update(n):
  return (n * 48271) % 2147483647


N = 40000000
count = 0
a_tmp = a
b_tmp = b
for i in range(N):
  a_tmp = a_update(a_tmp)
  b_tmp = b_update(b_tmp)
  if (a_tmp & 0xffff) == (b_tmp & 0xffff):
    count += 1

print(count)


N = 5000000
count = 0
a_tmp = a
b_tmp = b
for i in range(N):
  while True:
    a_tmp = a_update(a_tmp)
    if (a_tmp % 4) == 0:
      break
  while True:
    b_tmp = b_update(b_tmp)
    if (b_tmp % 8) == 0:
      break
  if (a_tmp & 0xffff) == (b_tmp & 0xffff):
    count += 1

print(count)
