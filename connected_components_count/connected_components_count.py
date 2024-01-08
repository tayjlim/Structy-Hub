def connected_components_count(graph):
  count = 0
  visited = set()
  for node in graph:
    print('this is the starting',node)
    if explore(graph,node,visited) == True:
      print('increment count',node)
      count +=1
  return count
​
​
def explore (graph, node, visited):
  if node in visited:
    return False
  
  visited.add(node)
  for neighbor in graph[node]:
    print('neighbor',neighbor)
    explore(graph,neighbor,visited)
  
  return True
  
connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2