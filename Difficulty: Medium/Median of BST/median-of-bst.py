class Solution:
    def findMedian(self, root):
        def inorder(node):
            return inorder(node.left) + [node.data] + inorder(node.right) if node else []
        arr = inorder(root)
        n = len(arr)
        if n % 2 == 0:
            return arr[(n // 2) - 1]
        else:
            return arr[n // 2]
