class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        sorted_arr = sorted(arr)
        
        # Precompute Catalan numbers
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        # Map value → index in sorted array
        index_map = {val: i for i, val in enumerate(sorted_arr)}
        
        result = []
        
        for val in arr:
            i = index_map[val]
            left = i
            right = n - i - 1
            result.append(catalan[left] * catalan[right])
        
        return result