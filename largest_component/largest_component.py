
def largest_component(graph):
  largest = 0
  visited = set()
  for node in graph:
    current_island = traverse(graph,node,visited) # this will return a number 
    if current_island > largest:
      largest = current_island
  return largest
​
def traverse(graph,node,visited):
  if node in visited:
    return 0
  
  visited.add(node)# if it isnt in visited we add the current node
  size = 1
  
  for neighbor in graph[node]:
    size += traverse(graph,neighbor,visited)
  return size
  
"""
last problem we coutned the nodes in one island in the directed graph.
this problem we are going to solve the biggest one
​
To this I think we are going to incremeent count on the traverse function
then in the largest  component function we will use the max of the current with current max 
"""
​
largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4