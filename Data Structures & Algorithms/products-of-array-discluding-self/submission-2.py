class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(nums)):
            temp=[]
            prod=1
            temp=nums.copy()
            temp.pop(i)
            for t in temp:
                prod*=t
            res.append(prod)

        return res