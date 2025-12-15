class Solution:
    def cntWays(self, arr):
        n = len(arr)
        
        even_pref = [0] * (n + 1)
        odd_pref = [0] * (n + 1)
        
        for i in range(n):
            even_pref[i + 1] = even_pref[i]
            odd_pref[i + 1] = odd_pref[i]
            if i % 2 == 0:
                even_pref[i + 1] += arr[i]
            else:
                odd_pref[i + 1] += arr[i]
        
        total_even = even_pref[n]
        total_odd = odd_pref[n]
        
        count = 0
        
        for i in range(n):
            even_before = even_pref[i]
            odd_before = odd_pref[i]
            
            even_after = total_odd - odd_pref[i + 1]
            odd_after = total_even - even_pref[i + 1]
            
            if even_before + even_after == odd_before + odd_after:
                count += 1
        
        return count
