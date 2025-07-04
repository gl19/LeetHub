class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            if abs(nums[0] - nums[i]) <= target:
                dp[i] = 1

        for i in range(1, n):
            if dp[i] > 0:
                for j in range(i + 1, n):
                    if abs(nums[i] - nums[j]) <= target:
                        dp[j] = max(dp[j], dp[i] + 1)

        if dp[-1] == 0:
            return -1

        return dp[-1]
