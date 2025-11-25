class Solution:
    def subarrayXor(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            if ((i + 1) * (n - i)) % 2 == 1:
                ans ^= arr[i]
        return ans
