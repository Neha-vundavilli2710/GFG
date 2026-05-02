class Solution:
    def findPosition(self, n):
        # code here 
        if (n & (n-1)) != 0 :
            return -1
        i = 0
        while n :
            n = n >> 1
            i += 1
        return i