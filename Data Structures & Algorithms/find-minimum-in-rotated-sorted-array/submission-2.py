class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb = 0
        rb = len(nums)-1    
        m = (lb+rb)//2
        if nums[lb] < nums[rb]:
            return nums[lb]
        while lb<rb:
            if nums[m]>=nums[lb] and nums[m]>nums[rb]:
                lb = m+1
            elif nums[m]<nums[rb]:
                rb = m
            else: 
                return nums[m]
            m = (lb+rb)//2
        return nums[m]

