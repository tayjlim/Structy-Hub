from collections import deque
​
def closest_carrot(grid, starting_row, starting_col):
  visited = set((starting_row,starting_col))
  queue = deque([(starting_row,starting_col,0)])
  
  while queue:
    curr_row,curr_col,distance = queue.popleft()
    print(curr_row,curr_col,distance)
    
    if grid[curr_row][curr_col] == 'C':
      return distance
    else:
      deltas = [(-1,0),(1,0),(0,1),(0,-1)]
      for delta in deltas:
            row,col = delta
            newRow,newCol = curr_row+row,col+curr_col
            # now we check here before we append
            if (newRow >=0 and newRow<len(grid)) and (newCol >= 0 and newCol < len(grid[0])):
              #one more if to see if it is an open space and not in visited
              if grid[newRow][newCol] != 'X' and (newRow,newCol) not in visited:
                print(newRow,newCol)
                print('true')
                visited.add((newRow,newCol))
                queue.append((newRow, newCol, distance + 1))
    
      
  return -1
      #over here we want to get the NEIGHBORS that are valid
    # a valid neighbor is in bounds of len(grid) and len(grid[0]) 
    # a valid neighbor is not in visited AND is O 
​
"""
current = (x,y,steps)
​
​
​
"""