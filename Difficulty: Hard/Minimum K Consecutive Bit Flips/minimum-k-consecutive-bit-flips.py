from collections import deque

class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flip = 0
        res = 0
        q = deque()  # store indices where flips expire
        
        for i in range(n):
            # Remove flips that have expired
            if q and q[0] == i:
                q.popleft()
                flip ^= 1
            
            # If current bit is 0 after flips
            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1
                res += 1
                flip ^= 1  # new flip applied
                q.append(i + k)  # flip effect expires after k elements
        
        return res