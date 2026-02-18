class Solution:
    def inversionCount(self, arr):
        self.count = 0
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    self.count += len(left) - i
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged
        
        merge_sort(arr)
        return self.count
