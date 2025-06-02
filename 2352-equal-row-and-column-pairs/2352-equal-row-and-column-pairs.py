class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_dict = {}
        for row in grid:
            # Tuple for hashing
            tuple_row = tuple(row)
            if tuple_row in row_dict:
                row_dict[tuple_row] += 1
            else:
                row_dict[tuple_row] = 1
                
        pairs = 0
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])

            tuple_col = tuple(col)
            if tuple_col in row_dict:
                pairs += row_dict[tuple_col]

        return pairs
