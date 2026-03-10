class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        nsr = [n] * n  # next smaller element to the right
        
        # Compute NSR using monotonic stack
        for i in range(n-1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                nsr[i] = stack[-1]
            stack.append(i)
        
        # Count valid subarrays
        count = 0
        for i in range(n):
            count += nsr[i] - i
        
        return count