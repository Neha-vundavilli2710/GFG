class Solution:
    def longestKSubstr(self, s, k):
        from collections import defaultdict
        
        n = len(s)
        count = defaultdict(int)
        left = 0
        max_len = -1
        
        for right in range(n):
            count[s[right]] += 1
            
            # Shrink window if more than k distinct
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            
            # Update max_len only when exactly k distinct
            if len(count) == k:
                max_len = max(max_len, right - left + 1)
        
        return max_len