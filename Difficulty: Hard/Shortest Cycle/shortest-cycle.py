from collections import deque, defaultdict

class Solution:
    def shortCycle(self, V, edges):
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = float('inf')

        # Run BFS from each vertex
        for start in range(V):
            dist = [-1] * V
            parent = [-1] * V
            dist[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        ans = min(ans, dist[u] + dist[v] + 1)

        return ans if ans != float('inf') else -1
