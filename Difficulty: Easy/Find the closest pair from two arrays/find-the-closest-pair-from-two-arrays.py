class Solution:
    def findClosestPair(self, arr1, arr2, x):
        i = 0
        j = len(arr2) - 1
        
        min_diff = float('inf')
        ans = [0, 0]
        
        while i < len(arr1) and j >= 0:
            
            s = arr1[i] + arr2[j]
            diff = abs(s - x)
            
            if diff < min_diff:
                min_diff = diff
                ans = [arr1[i], arr2[j]]
            
            if s > x:
                j -= 1
            else:
                i += 1
        
        return ans