from collections import Counter

class Solution:
    def minWindow(self, s: str, p: str) -> str:
        if not s or not p:
            return ""
        
        count_p = Counter(p)
        required = len(count_p)
        formed = 0
        window_counts = {}
        
        l = 0
        min_len = float('inf')
        start = 0
        
        for r, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in count_p and window_counts[char] == count_p[char]:
                formed += 1
            
            # Try to shrink the window from left
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                
                # Remove left char
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in count_p and window_counts[left_char] < count_p[left_char]:
                    formed -= 1
                
                l += 1
        
        return "" if min_len == float('inf') else s[start:start+min_len]