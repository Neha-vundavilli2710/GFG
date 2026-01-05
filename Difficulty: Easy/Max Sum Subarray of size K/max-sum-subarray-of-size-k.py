class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        
        # sum of first window
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        # sliding window
        for i in range(k, n):
            window_sum += arr[i]
            window_sum -= arr[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        
        return max_sum
