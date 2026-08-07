class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while (target!=nums[(end+start)//2]) and (end>start):
            if target>nums[(end+start)//2]:
                start=(end+start)//2+1
            elif target<nums[(end+start)//2]:
                end=(end+start)//2-1
        if target == nums[(end+start)//2]:
            return (end+start)//2
        else:
            return -1