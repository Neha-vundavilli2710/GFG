class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        if k > n:
            return 0
        
        curr_xor = 0
        # Compute initial XOR for first k elements
        for i in range(k):
            curr_xor ^= arr[i]
        
        max_xor = curr_xor
        
        # Slide the window
        for i in range(k, n):
            # Remove element leaving the window
            curr_xor ^= arr[i - k]
            # Add new element entering the window
            curr_xor ^= arr[i]
            max_xor = max(max_xor, curr_xor)
        
        return max_xor