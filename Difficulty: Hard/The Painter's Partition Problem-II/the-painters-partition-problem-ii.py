class Solution:
    def minTime(self, arr, k):
        low = max(arr)
        high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            painters = 1
            current_sum = 0
            
            for board in arr:
                if current_sum + board <= mid:
                    current_sum += board
                else:
                    painters += 1
                    current_sum = board
            
            if painters <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
