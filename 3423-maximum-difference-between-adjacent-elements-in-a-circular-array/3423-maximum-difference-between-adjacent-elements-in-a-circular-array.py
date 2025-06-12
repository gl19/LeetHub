class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            abs_diff = abs(nums[i] - nums[i - 1])
            if abs_diff > max_diff:
                max_diff = abs_diff

        return max_diff
