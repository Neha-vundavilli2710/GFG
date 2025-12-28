class Solution:
    def minTime(self, rank, n):

        def canMake(time):
            donuts = 0
            for r in rank:
                k = 1
                total = r
                while total <= time:
                    donuts += 1
                    k += 1
                    total += r * k
                if donuts >= n:
                    return True
            return False

        low = 0
        high = min(rank) * n * (n + 1) // 2
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canMake(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
