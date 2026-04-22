class Solution:

    def minSteps(self, m, n, d):

        from math import gcd

 

        # Impossible cases

        if d > max(m, n):

            return -1

        if d % gcd(m, n) != 0:

            return -1

 

        # If directly equal

        if d == m or d == n:

            return 1

 

        def solve(fromCap, toCap, target):

            fromJug = 0

            toJug = 0

            steps = 0

 

            while fromJug != target and toJug != target:

                

                # Fill fromJug

                if fromJug == 0:

                    fromJug = fromCap

                    steps += 1

 

                # Empty toJug

                elif toJug == toCap:

                    toJug = 0

                    steps += 1

 

                # Pour

                else:

                    transfer = min(fromJug, toCap - toJug)

                    toJug += transfer

                    fromJug -= transfer

                    steps += 1

 

            return steps

 

        return min(solve(m, n, d), solve(n, m, d))