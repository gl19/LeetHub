class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        set_nums = set(nums)
        for i in range(1, n + 1):
            if i not in set_nums:
                return i

        return max(nums) + 1
