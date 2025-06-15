class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique_permutations = set()
        def helper(permutation, remaining_nums):
            if len(remaining_nums) == 0:
               unique_permutations.add(tuple(permutation))
               return

            for i in range(len(remaining_nums)):
                helper(permutation + [remaining_nums[i]], remaining_nums[:i] + remaining_nums[i + 1:])

        helper([], nums)
        return list(unique_permutations)