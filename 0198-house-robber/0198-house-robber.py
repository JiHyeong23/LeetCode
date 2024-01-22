class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if i == 1:
                nums[1] = max(nums[0], nums[1])
            else:
                nums[i] = max(nums[i-1], nums[i]+nums[i-2])
        return nums[-1]