from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        # Map: horizontal distance → first node value
        hd_map = {}
        q = deque([(root, 0)])  # (node, hd)
        
        min_hd = max_hd = 0
        
        while q:
            node, hd = q.popleft()
            
            # Only take the first node at each horizontal distance
            if hd not in hd_map:
                hd_map[hd] = node.data
                min_hd = min(min_hd, hd)
                max_hd = max(max_hd, hd)
            
            if node.left:
                q.append((node.left, hd-1))
            if node.right:
                q.append((node.right, hd+1))
        
        # Collect nodes from leftmost hd to rightmost hd
        return [hd_map[i] for i in range(min_hd, max_hd+1)]