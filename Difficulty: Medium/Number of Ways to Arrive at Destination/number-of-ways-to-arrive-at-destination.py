import heapq

class Solution:
    def countPaths(self, V: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(V)]
        for u, v, time in edges:
            adj[u].append((v, time))
            adj[v].append((u, time))

        MOD = 10**9 + 7

        dist = [float('inf')] * V
        dist[0] = 0

        ways = [0] * V
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            t, u = heapq.heappop(pq)

            if t > dist[u]:
                continue

            for v, time_v in adj[u]:
                new_time = t + time_v

                if new_time < dist[v]:
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_time, v))

                elif new_time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[V - 1]