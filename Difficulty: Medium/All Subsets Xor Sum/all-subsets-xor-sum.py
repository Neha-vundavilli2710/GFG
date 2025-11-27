class Solution:
    def subsetXORSum(self, arr: list[int]) -> int:
        OR = 0
        for x in arr:
            OR |= x
        return OR * (1 << (len(arr) - 1))
