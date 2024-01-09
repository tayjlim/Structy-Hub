
from collections import deque
def shortest_path(edges, node_A, node_B):
  graph = makeGraph(edges)
  visited = set()
  queue = deque([(node_A,0)])
  visited.add(node_A)
  while queue:
    current =  queue.popleft()
    node,steps = current
 
    if node == node_B:
      return steps
    
    neighbors = graph[node]
    for neighbor in neighbors:
      if neighbor not in visited:
        # add it to the queue and add the neighbor to visited
        visited.add(neighbor)
        queue.append((neighbor,steps+1))
  return -1
​
def makeGraph(edges):
  graph= {}
  for edge in edges:
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
​
    graph[a].append(b)
    graph[b].append(a)
  return graph
​
"""
step 1. make a graph
      2. implement a queue because if we use BFS we are doing a level order traversal
      3. (node, steps) increment each step and append to the queue 
      4. We pop the node compare, repeat
"""