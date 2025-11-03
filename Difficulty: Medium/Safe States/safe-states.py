class Solution:
    def safeNodes(self, V: int, edges: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(V)]
        rev_graph = [[] for _ in range(V)]
        indegree = [0] * V

        # Build graph and reverse graph
        for u, v in edges:
            graph[u].append(v)
            rev_graph[v].append(u)
            indegree[u] += 1

        from collections import deque
        q = deque()

        # Terminal nodes (no outgoing edges in original graph)
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * V

        # Topological sort on reversed graph
        while q:
            node = q.popleft()
            safe[node] = True
            for prev in rev_graph[node]:
                indegree[prev] -= 1
                if indegree[prev] == 0:
                    q.append(prev)

        return [i for i in range(V) if safe[i]]
