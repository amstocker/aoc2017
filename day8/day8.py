with open('input.txt') as f:
  lines = [l.split()  for l in f.read().rstrip().split('\n')]

max_val = 0
regs = {}
for line in lines:
  reg = line[0]
  cmd = line[1]
  amt = int(line[2])
  tar = line[4]
  comp = line[5]
  comp_amt = int(line[6])

  if reg not in regs:
    regs[reg] = 0
  if tar not in regs:
    regs[tar] = 0

  tar_val = regs[tar]
  update = False
  if comp == "==" and tar_val == comp_amt:
    update = True
  elif comp == "!=" and tar_val != comp_amt:
    update = True
  elif comp == "<=" and tar_val <= comp_amt:
    update = True
  elif comp == ">=" and tar_val >= comp_amt:
    update = True
  elif comp == "<" and tar_val < comp_amt:
    update = True
  elif comp == ">" and tar_val > comp_amt:
    update = True

  if update:
    if cmd == "inc":
      regs[reg] += amt
    elif cmd == "dec":
      regs[reg] -= amt
  
  max_val = max(max_val, sorted(list(regs.items()), key=lambda x: -x[1])[0][1])

print(sorted(list(regs.items()), key=lambda x: -x[1]))
print(max_val)
