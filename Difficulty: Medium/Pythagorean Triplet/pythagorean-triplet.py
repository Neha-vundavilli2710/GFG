class Solution:
    def pythagoreanTriplet(self, arr):
        max_val = max(arr)
        size = max_val*max_val*2 + 1
        
        # Presence array for squares
        present = [False] * size
        for num in arr:
            present[num*num] = True
        
        n = len(arr)
        # Check all pairs
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i]*arr[i] + arr[j]*arr[j]
                if s < size and present[s]:
                    return True
        return False