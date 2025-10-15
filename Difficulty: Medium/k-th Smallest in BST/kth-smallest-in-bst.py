class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)
        arr = inorder(root)
        return arr[k - 1] if k <= len(arr) else -1
