class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA=0
        i=0
        j=len(heights)-1
        while i<j:
            
            maxA=max(maxA,(j-i)*min(heights[i],heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxA