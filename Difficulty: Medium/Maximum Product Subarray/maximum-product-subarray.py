class Solution:
    def maxProduct(self, arr):
        max_end = arr[0]
        min_end = arr[0]
        result = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            if x < 0:
                max_end, min_end = min_end, max_end

            max_end = max(x, max_end * x)
            min_end = min(x, min_end * x)

            result = max(result, max_end)

        return result
