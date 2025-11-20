class Solution:
    def minCost(self, s: str, t: str, transform: list, cost: list) -> int:
        if len(s) != len(t):
            return -1

        INF = 10**15
        dist = [[INF]*26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for (a, b), c in zip(transform, cost):
            u = ord(a) - 97
            v = ord(b) - 97
            dist[u][v] = min(dist[u][v], c)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total = 0
        for c1, c2 in zip(s, t):
            if c1 == c2:
                continue
            x = ord(c1) - 97
            y = ord(c2) - 97
            best = INF
            for mid in range(26):
                best = min(best, dist[x][mid] + dist[y][mid])
            if best >= INF:
                return -1
            total += best

        return total
