class Solution:
    def articulationPoints(self, V, edges):
        
        # Build graph
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        tin = [-1] * V
        low = [-1] * V
        visited = [False] * V
        timer = [0]
        
        result = set()
        
        def dfs(node, parent):
            visited[node] = True
            tin[node] = low[node] = timer[0]
            timer[0] += 1
            
            children = 0
            
            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if not visited[nei]:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    
                    # articulation condition
                    if parent != -1 and low[nei] >= tin[node]:
                        result.add(node)
                    
                    children += 1
                else:
                    low[node] = min(low[node], tin[nei])
            
            # root case
            if parent == -1 and children > 1:
                result.add(node)
        
        # handle disconnected graph
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)
        
        if not result:
            return [-1]
        
        return sorted(result)