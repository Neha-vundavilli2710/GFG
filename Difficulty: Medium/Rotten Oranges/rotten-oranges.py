from collections import deque

class Solution:
    def orangesRot(self, mat):   # ✅ renamed
        
        rows, cols = len(mat), len(mat[0])
        q = deque()
        fresh = 0
        
        # initialize
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        
        # BFS
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                        mat[nx][ny] = 2
                        q.append((nx, ny))
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1