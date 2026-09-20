class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        for i in range(len(nums)):
            if i==0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1]*nums[i])
        postfix=[0]*len(prefix)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix[i]=nums[i]
            else:
                postfix[i]=nums[i]*postfix[i+1]
        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(1*postfix[i+1])
            elif i==len(nums)-1:
                res.append(prefix[i-1]*1)
            else:
                res.append(prefix[i-1]*postfix[i+1])
        return res