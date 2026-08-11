class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        rb = len(nums) - 1

        while lb <= rb:
            m = (lb + rb) // 2

            if nums[m] == target:
                return m

            # Left half is sorted
            if nums[lb] <= nums[m]:
                if nums[lb] <= target < nums[m]:
                    rb = m - 1
                else:
                    lb = m + 1

            # Right half is sorted
            else:
                if nums[m] < target <= nums[rb]:
                    lb = m + 1
                else:
                    rb = m - 1

        return -1