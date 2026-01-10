class Solution:
    def countSubstr(self, s, k):
        def atMost(k):
            freq = {}
            left = 0
            res = 0
            distinct = 0
            for right in range(len(s)):
                if freq.get(s[right], 0) == 0:
                    distinct += 1
                freq[s[right]] = freq.get(s[right], 0) + 1
                while distinct > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1
            return res

        return atMost(k) - atMost(k - 1)
