SAMPLE = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

with open('input.txt') as f:
  lines = [line.rstrip() for line in f.read().rstrip().split('\n')]
  lines_sample = [line.rstrip() for line in SAMPLE.rstrip().split('\n')]


class Node:
  def __init__(self, name, weight, parent=None):
    self.name = name
    self.weight = weight
    self.parent = parent
    self.child_names = set()

  def tower_weight(self, node_map):
    weight = self.weight
    for name in self.child_names:
      if name in node_map:
        weight += node_map[name].tower_weight(node_map)
    return weight

  def set_parent(self, parent):
    self.parent = parent

  def add_child(self, child_name):
    self.child_names.add(child_name)
    
  def get_top(self):
    if self.parent:
      return self.parent.get_top()
    return self

  def __repr__(self):
    return "Node({}, {}, {}, {})".format(self.name,
                                         self.weight,
                                         self.parent and self.parent.name,
                                         self.child_names)


def node_from_line(line):
  parts = line.split()
  node = Node(parts[0],
              int(parts[1][1:-1]))
  if len(parts) > 3:
    for child_name in parts[3:]:
      node.add_child(child_name.rstrip(','))
  return node
    

# part 1
nodes = {}
for line in lines:
  new_node = node_from_line(line)
  for node_name, node in nodes.items():
    if new_node.name in node.child_names:
      new_node.set_parent(node)
    if node_name in new_node.child_names:
      node.set_parent(new_node)
  nodes[new_node.name] = new_node

root = new_node.get_top()
print(root.name)


# part 2 (just did this visually)
def weight_helper(node, tab=0):
  print("{}{} : {}".format(tab * '|\t', node, node.tower_weight(nodes)))
  for child_name in node.child_names:
    weight_helper(nodes[child_name], tab + 1)

weight_helper(root)
