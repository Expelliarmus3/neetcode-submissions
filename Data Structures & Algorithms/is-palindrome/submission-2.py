class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=list(s)
        l=[]
        for ele in s1:
            if ele.isalnum():
                l.append(str.lower(ele))
        left=0
        right=len(l)-1
        while left<right:
            if l[left]!=l[right]:
                return False
            left+=1
            right-=1
        return True

