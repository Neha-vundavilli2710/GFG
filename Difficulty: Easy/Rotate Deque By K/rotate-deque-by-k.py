from collections import deque

class Solution:
    def rotateDeque(self, dq: deque, rTyp: int, k: int):
        if not dq:
            return dq
        n = len(dq)
        k %= n
        if rTyp == 1:
            dq.rotate(k)
        else:
            dq.rotate(-k)
        return dq
