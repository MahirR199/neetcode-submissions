class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = [nums[0]]
        for i in range(1,len(nums)):
            for j in range(len(nums2)):
                if nums[i]+nums2[j]==target and i!=j:
                    return [j,i]
            nums2.append(nums[i])