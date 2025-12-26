class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)
        
        # If kth missing number is after the last element
        if arr[-1] - n < k:
            return arr[-1] + (k - (arr[-1] - n))
        
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                low = mid + 1
            else:
                high = mid
        
        return k + low
