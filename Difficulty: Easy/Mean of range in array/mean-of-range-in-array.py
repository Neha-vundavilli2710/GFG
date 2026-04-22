class Solution:
    def findMean(self, arr, queries):
        # code here
        res = []
        c_sum = [0]*len(arr)
        for i in range(1, len(arr)):
            c_sum[i] = arr[i-1]+c_sum[i-1]
        
        for l, r in queries:
            total = c_sum[r] + arr[r] - c_sum[l]
            total //= (r-l+1)
            res.append(total)
            
        return res