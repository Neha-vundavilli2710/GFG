class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        res = ""
        min_len = float("inf")

        for i in range(n):
            if s1[i] != s2[0]:
                continue
            j = i
            k = 0
            while j < n and k < m:
                if s1[j] == s2[k]:
                    k += 1
                j += 1
            if k < m:
                continue
            end = j - 1
            k = m - 1
            j = end
            while j >= i:
                if s1[j] == s2[k]:
                    k -= 1
                    if k < 0:
                        break
                j -= 1
            start = j
            if end - start + 1 < min_len:
                min_len = end - start + 1
                res = s1[start:end + 1]
        return res
