class Solution:
    def longestSubarray(self, arr, k):
        prefix = 0
        first_seen = {}
        max_len = 0
        
        for i in range(len(arr)):
            # Transform values
            if arr[i] > k:
                prefix += 1
            else:
                prefix -= 1
            
            # If prefix positive → subarray from 0 works
            if prefix > 0:
                max_len = i + 1
            
            # Store first occurrence
            if prefix not in first_seen:
                first_seen[prefix] = i
            
            # Check prefix-1 existence
            if (prefix - 1) in first_seen:
                max_len = max(max_len, i - first_seen[prefix - 1])
        
        return max_len