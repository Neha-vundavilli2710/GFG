class Solution:
    def maxSum(self, arr):
        n = len(arr)
        arr_sum = sum(arr)

        curr_val = 0
        for i in range(n):
            curr_val += i * arr[i]

        max_val = curr_val

        for i in range(1, n):
            curr_val = curr_val + arr_sum - n * arr[n - i]
            max_val = max(max_val, curr_val)

        return max_val
