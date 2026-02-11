class Solution:
    def minCost(self, heights, cost):
        pairs = sorted(zip(heights, cost))
        
        total_cost = sum(cost)
        prefix = 0
        median = 0

        for h, c in pairs:
            prefix += c
            if prefix >= total_cost / 2:
                median = h
                break

        ans = 0
        for h, c in pairs:
            ans += abs(h - median) * c

        return ans
