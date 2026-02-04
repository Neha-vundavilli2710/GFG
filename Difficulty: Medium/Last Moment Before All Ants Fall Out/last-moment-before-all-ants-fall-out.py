class Solution:
    def getLastMoment(self, n, left, right):
        t = 0
        if left:
            t = max(t, max(left))
        if right:
            t = max(t, max(n - x for x in right))
        return t
