from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        hd_map = defaultdict(list)
        q = deque([(root, 0)])  # node, horizontal distance
        min_hd = max_hd = 0
        
        while q:
            node, hd = q.popleft()
            
            hd_map[hd].append(node.data)
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            if node.left:
                q.append((node.left, hd-1))
            if node.right:
                q.append((node.right, hd+1))
        
        return [hd_map[hd] for hd in range(min_hd, max_hd+1)]