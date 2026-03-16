from collections import defaultdict

class Solution:
    def countAllPaths(self, root, k):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # base case: path sum = 0
        self.result = 0
        
        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum += node.data  # use .data instead of .val
            self.result += prefix_count[curr_sum - k]
            
            prefix_count[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix_count[curr_sum] -= 1  # backtrack
        
        dfs(root, 0)
        return self.result