from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2

        dq = deque(q)
        first = deque()
        second = deque()

        for _ in range(half):
            first.append(dq.popleft())
        while dq:
            second.append(dq.popleft())

        i = 0
        while first and second:
            q[i] = first.popleft()
            q[i+1] = second.popleft()
            i += 2
