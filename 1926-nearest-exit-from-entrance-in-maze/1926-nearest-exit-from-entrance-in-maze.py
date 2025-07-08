class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        to_visit = [(entrance, 0)]
        visited = set()

        def is_exit(i, j):
            return entrance != [i, j] and (i == 0 or i == (m - 1) or j == 0 or j == (n - 1))

        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n and \
                maze[i][j] == '.' and (i, j) not in visited

        
        while to_visit:
            (i, j), moves = to_visit.pop(0)
            if is_exit(i, j):
                return moves

            visited.add((i, j))

            if is_valid(i + 1, j):
                to_visit.append(((i + 1, j), moves + 1))

            if is_valid(i, j + 1):
                to_visit.append(((i, j + 1), moves + 1))

            if is_valid(i - 1, j):
                to_visit.append(((i - 1, j), moves + 1))

            if is_valid(i, j - 1):
                to_visit.append(((i, j - 1), moves + 1))               

        return -1