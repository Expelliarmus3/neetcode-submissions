class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for num in nums:
            #Finding the start value
            if (num-1) not in numSet:
                length=0
                #growing once we find the start
                while(num+length) in numSet:
                    length+=1
                longest=max(longest,length)
        return longest