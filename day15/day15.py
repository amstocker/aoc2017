a = 699
b = 124

def a_update(n):
  return (n * 16807) % 2147483647

def b_update(n):
  return (n * 48271) % 2147483647


N = 40000000
count = 0
for i in range(N):
  if (i % 100000) == 0:
    print(i)
  a = a_update(a)
  b = b_update(b)

  if (a & 0xffff) == (b & 0xffff):
    count += 1

print(count)


N = 5000000
count = 0
for i in range(N):
  if (i % 100000) == 0:
    print(i)

  while True:
    a = a_update(a)
    if (a % 4) == 0:
      break

  while True:
    b = b_update(b)
    if (b % 8) == 0:
      break

  if (a & 0xffff) == (b & 0xffff):
    count += 1

print(count)
