class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        best = [[float(inf) for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 1 and j == 2:
                    print(best)
                if i == 0 and j == 0:
                    best[i][j] = grid[i][j]
                elif i == 0:    
                    best[i][j] = grid[i][j] + best[i][j - 1]
                elif j == 0:
                    best[i][j] = grid[i][j] + best[i - 1][j]
                else:
                    best[i][j] = grid[i][j] + min(best[i][j - 1], best[i - 1][j])

        return best[-1][-1]