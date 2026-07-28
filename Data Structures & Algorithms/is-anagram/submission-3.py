class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            dict1={}
            dict2={}
            set1=set(s)
            set2=set(t)
            for i in set1:
                dict1[i]=0
            for j in set2:
                dict2[j]=0
            for i in s:
                dict1[i]+=1
            for j in t:
                dict2[j]+=1
            if dict1==dict2:
                return True
            else:
                return False
