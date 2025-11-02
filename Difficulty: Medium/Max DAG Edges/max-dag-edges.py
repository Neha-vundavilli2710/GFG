from collections import defaultdict, deque

class Solution:
    def maxEdgesToAdd(self, V, edges):
        graph = defaultdict(list)
        indegree = [0]*V

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Topological Sort
        q = deque([i for i in range(V) if indegree[i] == 0])
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        pos = {topo[i]: i for i in range(V)}

        # Count existing forward edges (u before v)
        existing = 0
        for u, v in edges:
            if pos[u] < pos[v]:
                existing += 1

        total_possible = V*(V-1)//2
        return total_possible - existing
