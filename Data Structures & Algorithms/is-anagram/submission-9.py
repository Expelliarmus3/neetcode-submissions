class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls1=list(s)
        ls2=list(t)
        ls1=set(ls1)
        ls2=set(ls2)
        dict1=collections.defaultdict(int,{k:0 for k in ls1})
        dict2=collections.defaultdict(int,{k:0 for k in ls2})
        for st in s:
            dict1[st]+=1
        for st in t:
            dict2[st]+=1
        return (dict1==dict2)