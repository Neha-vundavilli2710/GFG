from collections import deque

class Solution:
    def diameter(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            q = deque([(start, 0)])
            visited = [False] * V
            visited[start] = True
            far_node, max_dist = start, 0

            while q:
                node, dist = q.popleft()
                if dist > max_dist:
                    max_dist, far_node = dist, node
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append((nei, dist + 1))
            return far_node, max_dist

        farthest_node, _ = bfs(0)
        _, diameter = bfs(farthest_node)
        return diameter
