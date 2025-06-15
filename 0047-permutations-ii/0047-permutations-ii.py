class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        used = [False] * n
        def helper(permutation):
            if len(permutation) == n:
                result.append(list(permutation))
                return

            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                permutation.append(nums[i])
                helper(permutation)
                permutation.pop()
                used[i] = False

        helper([])
        return result