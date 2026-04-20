class Solution:
     def derangeCount(self, n: int) -> int:
          # code here
          if n == 1: return 0
          elif n == 2: return 1
          return (n-1) * (self.derangeCount(n-1) + self.derangeCount(n-2))