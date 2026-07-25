class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1

        res = 0
        while l<r:
            left = heights[l]
            right = heights[r]
            res = max(min(left,right)*(r-l), res)
            if(min(left,right) == left):
                l += 1
            else: 
                r-=1
        return res 