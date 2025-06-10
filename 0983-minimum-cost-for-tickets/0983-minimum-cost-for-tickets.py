class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        days_set = set(days)
        dp = [float("inf")] * (max_day + 1)
        dp[0] = 0
        for i in range(1, max_day + 1):
            if i in days_set:
                for j in range(30):
                    if i + j > max_day:
                        break

                    if j == 0:
                        dp[i] = min(dp[i + j], dp[i - 1] + min(costs))
                    elif j < 7:
                        dp[i + j] = min(dp[i + j], dp[i - 1] + min(costs[1:]))
                    elif j < 30:
                        dp[i + j] = min(dp[i + j], dp[i - 1] + costs[2])
            else:
                dp[i] = dp[i - 1]

        return dp[-1]