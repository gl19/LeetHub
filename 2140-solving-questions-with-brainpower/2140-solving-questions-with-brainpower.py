class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        ans = 0
        for i, (points, brainpower) in enumerate(questions):
            # solve
            if i + brainpower + 1 < n:
                dp[i + brainpower + 1] = max(dp[i + brainpower + 1], dp[i] + points)
            else:
                ans = max(ans, dp[i] + points)

            # skip
            if i + 1 < n:
                dp[i + 1] = max(dp[i + 1], dp[i])

        return ans
