class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            d1=collections.defaultdict(int)
            d2=collections.defaultdict(int)
            for i in list(s):
                d1[i]+=1
            for i in list(t):
                d2[i]+=1
            if d1==d2:
                return True
            else:
                return False