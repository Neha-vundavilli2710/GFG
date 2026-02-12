class Solution:
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        def can_make(target):
            temp = arr[:]
            add = [0] * (n + 1)
            curr_add = 0
            days_used = 0

            for i in range(n):
                curr_add += add[i]
                temp[i] += curr_add

                if temp[i] < target:
                    need = target - temp[i]
                    days_used += need
                    if days_used > k:
                        return False

                    curr_add += need
                    if i + w < n:
                        add[i + w] -= need

            return True

        left = min(arr)
        right = min(arr) + k
        ans = left

        while left <= right:
            mid = (left + right) // 2
            if can_make(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
