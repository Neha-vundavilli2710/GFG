class Solution:
    def topKFreq(self, arr, k):
        from collections import Counter
        freq = Counter(arr)
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
        return [num for num, _ in sorted_items[:k]]
