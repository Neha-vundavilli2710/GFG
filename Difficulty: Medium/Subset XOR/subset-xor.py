class Solution:
    def subsetXOR(self, n: int) -> list[int]:
        def xor_upto(x):
            if x % 4 == 0: return x
            if x % 4 == 1: return 1
            if x % 4 == 2: return x + 1
            return 0

        T = xor_upto(n)

        if T == n:
            return list(range(1, n + 1))

        target = T ^ n

        if 1 <= target <= n:
            return [i for i in range(1, n + 1) if i != target]

        a_remove, b_remove = None, None
        for a in range(1, n + 1):
            b = a ^ target
            if b > a and 1 <= b <= n:
                a_remove, b_remove = a, b
                break

        res = []
        for i in range(1, n + 1):
            if i == a_remove or i == b_remove:
                continue
            res.append(i)

        return res
