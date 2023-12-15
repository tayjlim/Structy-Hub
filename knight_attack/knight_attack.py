from collections import deque
​
def knight_attack(n, kr, kc, pr, pc):
    # Edge cases:
        #if all combinations tried, return None
        #if board size is less < than 2, return None (Knight cant move less than 2 vertically)
        #if knight position and pawn position are the same, return None since its already attacking
    if n < 2 or (kr, kc) == (pr, pc):
        return None
​
    #?I guess use a queue
    queue = deque([(kr, kc, 0)])
    #?Save what was visited in a set, lookup condition to stop it from returning
    visited = set()
​
    #Some DFS
    #Knight can only move horizontally +/- 1 and vertically +/- 2 (8 total possibilities)
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
​
    while queue:
        #Keep start position of knight with dist 0
        #get front element of queue, which is (r, c) that knight is going to
        #loop to check all possible moves from current position
        row, col, dist = queue.popleft()
        
        #Add a check if the knight and the pawn are on the same square (already attacking)
        if (row, col) == (pr, pc):
            return dist
       
        for delta_row, delta_col in moves:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist+1))
    return None