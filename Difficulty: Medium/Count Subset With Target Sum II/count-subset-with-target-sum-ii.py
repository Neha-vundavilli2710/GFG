from collections import Counter

class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        def gen(nums, idx, curr, res):
            if idx == len(nums):
                res.append(curr)
                return
            gen(nums, idx+1, curr, res)
            gen(nums, idx+1, curr + nums[idx], res)

        L = []
        R = []
        gen(left, 0, 0, L)
        gen(right, 0, 0, R)

        freq = Counter(R)

        ans = 0
        for s in L:
            ans += freq[k - s]

        return ans
