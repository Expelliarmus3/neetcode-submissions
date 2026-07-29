class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(f'{len(s)}#{s}')
        strs="".join(res)
        print(strs)
        return strs
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            start=j+1
            end=start+length
            res.append(s[start:end])
            i=end
        print(res)
        return res
        