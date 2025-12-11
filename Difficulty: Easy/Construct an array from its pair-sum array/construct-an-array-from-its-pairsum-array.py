import math

class Solution:
    def constructArr(self, arr):
        m = len(arr)

        # If there is only one pair-sum, original array has exactly 2 numbers
        if m == 1:
            return [1, arr[0] - 1]

        # Find n from m = n*(n-1)/2
        n = (1 + math.isqrt(1 + 8 * m)) // 2

        res = [0] * n

        # res[0] using: arr[0] = a0 + a1, arr[1] = a0 + a2, arr[n-1] = a1 + a2
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2

        # Now res[i] = (a0 + ai) - a0
        for i in range(1, n):
            res[i] = arr[i - 1] - res[0]

        return res