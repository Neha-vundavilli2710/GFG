class Solution:
    def countDistinct(self, arr, k):
        from collections import defaultdict
        n = len(arr)
        freq = defaultdict(int)
        res = []
        distinct = 0

        for i in range(k):
            if freq[arr[i]] == 0:
                distinct += 1
            freq[arr[i]] += 1
        res.append(distinct)

        for i in range(k, n):
            out = arr[i - k]
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1

            if freq[arr[i]] == 0:
                distinct += 1
            freq[arr[i]] += 1

            res.append(distinct)

        return res
