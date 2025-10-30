class Solution:
    def fill(self, grid):
        from collections import deque
        n, m = len(grid), len(grid[0])
        q = deque()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Step 1: Add boundary 'O's
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == 'O':
                    q.append((i, j))
        
        # Step 2: Mark connected 'O's from boundary as safe ('#')
        while q:
            x, y = q.popleft()
            if grid[x][y] != 'O':
                continue
            grid[x][y] = '#'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'O':
                    q.append((nx, ny))
        
        # Step 3: Flip surrounded 'O's and restore safe ones
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == '#':
                    grid[i][j] = 'O'
        
        return grid
