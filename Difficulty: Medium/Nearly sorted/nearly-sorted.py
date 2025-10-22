import heapq

class Solution:
    def nearlySorted(self, arr, k):
        heap = arr[:k+1]
        heapq.heapify(heap)
        index = 0
        for i in range(k+1, len(arr)):
            arr[index] = heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
            index += 1
        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1
        return arr
