import heapq

class Solution:
    def shortestPath(self, V: int, a: int, b: int, edges: list[list[int]]) -> int:
        g = [[] for _ in range(V)]
        for x, y, w1, w2 in edges:
            g[x].append((y, w1, w2))
            g[y].append((x, w1, w2))

        INF = 10**18
        dist = [[INF, INF] for _ in range(V)]
        dist[a][0] = 0

        pq = [(0, a, 0)]
        while pq:
            d, u, used = heapq.heappop(pq)
            if d > dist[u][used]:
                continue

            for v, w1, w2 in g[u]:
                nd = d + w1
                if nd < dist[v][used]:
                    dist[v][used] = nd
                    heapq.heappush(pq, (nd, v, used))

                if used == 0:
                    nd2 = d + w2
                    if nd2 < dist[v][1]:
                        dist[v][1] = nd2
                        heapq.heappush(pq, (nd2, v, 1))

        ans = min(dist[b][0], dist[b][1])
        return ans if ans < INF else -1
