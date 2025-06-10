class Solution:
    def numDecodings(self, s: str) -> int:
        # options:
        # take 1 or two if possible
        # edge case: zero is first
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] += 1
        nums = [int(c) for c in s]
        for i, num in enumerate(nums):
            if num == 0:
                continue
            elif num == 1 and i + 2 <= n:
                dp[i + 2] += dp[i]
            elif num == 2 and i + 2 <= n and nums[i + 1] <= 6:
                dp[i + 2] += dp[i]

            dp[i + 1] += dp[i]

        return dp[-1]


        