class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        seen=[]
        for i in range(len(strs)):
            if(strs[i] in seen):
                continue
            seen.append(strs[i])
            list1=[]
            list1.append(strs[i])
            for j in range(i+1,len(strs)):
                if (sorted(strs[i])==sorted(strs[j])):
                    list1.append(strs[j])
                    seen.append(strs[j])
            result.append(list1)
        return result