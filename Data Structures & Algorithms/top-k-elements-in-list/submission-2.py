class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Making hash function
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        print(hash)

        sorted_val= sorted(hash.keys(),key=hash.get,reverse=True)
        return sorted_val[:k]
