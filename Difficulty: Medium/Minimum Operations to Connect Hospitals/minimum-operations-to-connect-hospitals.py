class Solution:
    def minConnect(self, V: int, edges: list[list[int]]) -> int:
        if len(edges) < V - 1:
            return -1

        parent = list(range(V))
        rank = [0] * V

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        for u, v in edges:
            union(u, v)

        comp = sum(1 for i in range(V) if find(i) == i)
        return comp - 1
