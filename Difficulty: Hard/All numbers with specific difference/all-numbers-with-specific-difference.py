class Solution:
    def getCount(self, n, d):
        
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        
        left, right = 1, n
        ans = n + 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid - digit_sum(mid) >= d:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if ans > n:
            return 0
        
        return n - ans + 1
