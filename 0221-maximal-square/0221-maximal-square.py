class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        biggest = 0
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] > biggest:
                biggest = dp[0][j]

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] > biggest:
                biggest = dp[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

                    if dp[i][j] > biggest:
                        biggest = dp[i][j]
        
        return biggest ** 2