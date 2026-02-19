class Solution:
    def missingRange(self, arr, low, high):
        present = set(arr)
        result = []
        
        for num in range(low, high + 1):
            if num not in present:
                result.append(num)
        
        return result
