class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        if s.isalnum():
            s.replace(" ","")
            s1=s[::-1]
            return s==s1

        s= "".join(char for char in s if char.isalnum())
        print(s)
        c2=s[::-1]
       
        return s==c2
