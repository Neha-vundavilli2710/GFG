from collections import Counter, defaultdict

class Solution:
    def isPossible(self, arr, k):
        freq = Counter(arr)
        need = defaultdict(int)
        for num in sorted(arr):
            while freq[num] > 0:
                if need[num] > 0:
                    need[num] -= 1
                    need[num + 1] += 1
                    freq[num] -= 1
                else:
                    for x in range(num, num + k):
                        if freq[x] <= 0:
                            return False
                        freq[x] -= 1
                    need[num + k] += 1
        return True
