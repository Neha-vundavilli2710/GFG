class Solution:
    def findKRotation(self, arr):
        left, right = 0, len(arr) - 1

        while left <= right:
            if arr[left] <= arr[right]:
                return left

            mid = (left + right) // 2
            next_idx = (mid + 1) % len(arr)
            prev_idx = (mid - 1 + len(arr)) % len(arr)

            if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
                return mid
            elif arr[mid] >= arr[left]:
                left = mid + 1
            else:
                right = mid - 1

        return 0
