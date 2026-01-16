class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []

        for i, x in enumerate(arr):
            if x != -1:
                l = max(0, i - x)
                r = min(n - 1, i + x)
                intervals.append((l, r))

        intervals.sort()

        ans = 0
        i = 0
        curr = 0
        far = -1

        while curr <= n - 1:
            while i < len(intervals) and intervals[i][0] <= curr:
                far = max(far, intervals[i][1])
                i += 1

            if far < curr:
                return -1

            ans += 1
            curr = far + 1

        return ans
