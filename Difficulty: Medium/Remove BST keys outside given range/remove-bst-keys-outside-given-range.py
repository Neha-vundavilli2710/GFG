class Solution:
    def removekeys(self, root, l, r):
        if not root:
            return None

        # If current node's data is less than l, skip left subtree
        if root.data < l:
            return self.removekeys(root.right, l, r)

        # If current node's data is greater than r, skip right subtree
        if root.data > r:
            return self.removekeys(root.left, l, r)

        # Otherwise, recursively fix left and right subtrees
        root.left = self.removekeys(root.left, l, r)
        root.right = self.removekeys(root.right, l, r)
        return root
