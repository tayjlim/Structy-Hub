def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for node in graph[src]:
    if has_path(graph,node,dst) == True:
      return True
  
  return False