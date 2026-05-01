import heapq
class Solution:
    def kthLargest(self, arr, k):
        # code here 
        
        min_heap = []
        res = []
        for num in arr:
            heapq.heappush(min_heap, num)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
            if len(min_heap) == k:
                res.append(min_heap[0])
            else:
                res.append(-1)
                
        return res