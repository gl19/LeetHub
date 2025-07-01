class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        path = []
        def helper(start, width, height):
            if width <= 0 or height <= 0:
                return

            x, y = start
            for i in range(width):
                path.append(matrix[y][x + i])

            x += width - 1
            for i in range(1, height):
                path.append(matrix[y + i][x])

            if height <= 1:
                return

            y += height - 1
            for i in range(1, width):
                path.append(matrix[y][x - i])

            if width <= 1:
                return

            x = start[0]
            for i in range(1, height - 1):
                path.append(matrix[y - i][x])

            helper((start[0] + 1, start[1] + 1), width - 2, height - 2)

        helper((0,0), len(matrix[0]), len(matrix))
        return path