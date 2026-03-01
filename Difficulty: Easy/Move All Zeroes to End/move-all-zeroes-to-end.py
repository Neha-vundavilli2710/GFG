class Solution:
    def pushZerosToEnd(self, arr):
        j = 0  # next position for non-zero element
        
        # Move non-zero elements forward
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        
        # Fill remaining positions with 0
        for i in range(j, len(arr)):
            arr[i] = 0
        
        return arr  # returning for convenience