import heapq

class Solution:
    def minCostPath(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        dist = [[10**18] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            d, x, y = heapq.heappop(pq)
            if d > dist[x][y]:
                continue
            if x == n - 1 and y == m - 1:
                return d
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    cost = abs(mat[nx][ny] - mat[x][y])
                    nd = max(d, cost)
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heapq.heappush(pq, (nd, nx, ny))

        return dist[n - 1][m - 1]
