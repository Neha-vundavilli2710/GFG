class Solution:
    def nextFreqGreater(self, arr):
        n = len(arr)
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        res = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
                stack.pop()
            if stack:
                res[i] = arr[stack[-1]]
            stack.append(i)

        return res
