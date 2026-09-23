class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for i in range(len(s)):
            if s[i].isalnum():
                res.append(s[i].lower())
        print(res)
        i=0
        j=len(res)-1
        while(i<=j):
            if res[i]!=res[j]:
                return False
            i+=1
            j-=1
        return True