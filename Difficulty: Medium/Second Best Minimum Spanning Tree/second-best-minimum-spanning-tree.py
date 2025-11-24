class Solution:
    def secondMST(self, V, edges):
        edges_sorted = sorted(edges, key=lambda x: x[2])

        parent = list(range(V))
        rank = [0]*V

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1
            return True

        mst_edges = []
        mst_weight = 0

        for u, v, w in edges_sorted:
            if union(u, v):
                mst_edges.append((u, v, w))
                mst_weight += w

        if len(mst_edges) != V - 1:
            return -1

        best = float("inf")

        for rem_u, rem_v, rem_w in mst_edges:

            parent = list(range(V))
            rank = [0]*V
            total = 0
            count = 0

            for u, v, w in edges_sorted:
                if (u, v, w) == (rem_u, rem_v, rem_w):
                    continue
                if union(u, v):
                    total += w
                    count += 1
                if count == V - 1:
                    break

            if count == V - 1 and total > mst_weight:
                best = min(best, total)

        return best if best != float("inf") else -1
