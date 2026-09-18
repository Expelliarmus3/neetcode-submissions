class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp=defaultdict(int) #initializes with 0
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            hp[num]+=1
        for n,c in hp.items():
            freq[c].append(n) #inverted index and values
        res=[]
        for i in range(len(freq)-1,0,-1): #we need most frequent
            for n in freq[i]: #getting items from inner list
                res.append(n)
                if len(res)==k:
                    return res
        return[]