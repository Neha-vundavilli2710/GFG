from collections import deque, defaultdict

class Solution:
    def findOrder(self, n, prerequisites):
        adj = defaultdict(list)
        indegree = [0] * n

        # Build graph
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1

        # Queue for courses with no prerequisites
        q = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []

        while q:
            node = q.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If all courses are covered, return order
        if len(topo_order) == n:
            return topo_order
        else:
            return []
