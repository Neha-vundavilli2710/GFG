class Solution:
    def longestCycle(self, V, edges):
        
        # Step 1: create outgoing edge mapping
        graph = [-1] * V
        for u, v in edges:
            graph[u] = v
        
        visited = [False] * V
        ans = -1
        
        for i in range(V):
            if visited[i]:
                continue
            
            curr = i
            step = 0
            node_time = {}
            
            # traverse path
            while curr != -1 and not visited[curr]:
                visited[curr] = True
                node_time[curr] = step
                step += 1
                curr = graph[curr]
            
            # cycle detected
            if curr != -1 and curr in node_time:
                cycle_len = step - node_time[curr]
                ans = max(ans, cycle_len)
        
        return ans