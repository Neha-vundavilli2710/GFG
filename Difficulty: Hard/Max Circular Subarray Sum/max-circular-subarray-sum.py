class Solution:
    def maxCircularSum(self, arr):
        total = 0
        max_kadane = arr[0]
        curr_max = 0
        min_kadane = arr[0]
        curr_min = 0

        for x in arr:
            curr_max = max(x, curr_max + x)
            max_kadane = max(max_kadane, curr_max)

            curr_min = min(x, curr_min + x)
            min_kadane = min(min_kadane, curr_min)

            total += x

        if max_kadane < 0:
            return max_kadane

        return max(max_kadane, total - min_kadane)
