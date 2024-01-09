
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