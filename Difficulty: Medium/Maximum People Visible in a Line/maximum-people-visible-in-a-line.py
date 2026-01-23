class Solution:
    def maxPeople(self, arr: list[int]) -> int:
        n = len(arr)
        res = [1] * n
        
        # Left side visibility
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                # Person i can see everything from stack[-1] + 1 to i - 1
                res[i] += (i - stack[-1] - 1)
            else:
                # Person i can see everyone from 0 to i - 1
                res[i] += i
            stack.append(i)
            
        # Right side visibility
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                # Person i can see everything from i + 1 to stack[-1] - 1
                res[i] += (stack[-1] - i - 1)
            else:
                # Person i can see everyone from i + 1 to n - 1
                res[i] += (n - 1 - i)
            stack.append(i)
            
        return max(res)
