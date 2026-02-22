class Solution:
    def subarrayXor(self, arr, k):
        freq = {}
        prefix_xor = 0
        count = 0
        
        for num in arr:
            prefix_xor ^= num
            
            # Case when subarray starts from index 0
            if prefix_xor == k:
                count += 1
            
            # Check if (prefix_xor ^ k) seen before
            if (prefix_xor ^ k) in freq:
                count += freq[prefix_xor ^ k]
            
            # Store prefix_xor frequency
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count