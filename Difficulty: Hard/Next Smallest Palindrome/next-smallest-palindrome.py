class Solution:
    def nextPalindrome(self, num):
        
        # code here
        n=len(num)
        left,right=0,n-1
        
        copy_num=num[:]
        while left<right:
            copy_num[right]=copy_num[left]
            left+=1
            right-=1

        if copy_num>num:
            return copy_num
        
        mid = (n-1)//2
        left =mid
        right = mid if n%2==1 else mid+1
        carry = 1
        
        while left>=0 and carry:
            
            val= copy_num[left]+carry
            copy_num[left]=val%10
            carry=val//10
            copy_num[right]=copy_num[left]
            left-=1
            right+=1
                
        if carry:
            return [1]+[0]*(n-1)+[1]
        return copy_num 