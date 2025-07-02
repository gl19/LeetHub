class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        cur_island = 1
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        island_sizes = [[(0, 0)] * n for _ in range(m)]

        for j in range(m):
            for i in range(n):
                if visited[j][i] == False and grid[j][i] == 1:
                    count = 0
                    to_visit = [(i, j)]
                    marked = []

                    while to_visit:
                        x, y = to_visit.pop()
                        if visited[y][x]:
                            continue

                        visited[y][x] = True
                        marked.append((x, y)) 
                        count += 1

                        if x - 1 >= 0 and grid[y][x - 1] == 1 and visited[y][x - 1] == False:
                            to_visit.append((x - 1, y))

                        if y - 1 >= 0 and grid[y - 1][x] == 1 and visited[y - 1][x] == False:
                            to_visit.append((x, y - 1))

                        if x + 1 < n and grid[y][x + 1] == 1 and visited[y][x + 1] == False:
                            to_visit.append((x + 1, y))

                        if y + 1 < m and grid[y + 1][x] == 1 and visited[y + 1][x] == False:
                            to_visit.append((x, y + 1))

                    for (x, y) in marked:
                        island_sizes[y][x] = (count, cur_island)

                    cur_island += 1

        max_island_size = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 0:
                    size = 1
                    islands_added = set()
                    if x - 1 >= 0 and island_sizes[y][x - 1][0] > 0:
                        size += island_sizes[y][x - 1][0]
                        islands_added.add(island_sizes[y][x - 1][1])

                    if y - 1 >= 0 and island_sizes[y - 1][x][0] > 0 and island_sizes[y - 1][x][1] not in islands_added:
                        size += island_sizes[y - 1][x][0]
                        islands_added.add(island_sizes[y - 1][x][1])

                    if x + 1 < n and island_sizes[y][x + 1][0] > 0 and island_sizes[y][x + 1][1] not in islands_added:
                        size += island_sizes[y][x + 1][0]
                        islands_added.add(island_sizes[y][x + 1][1])

                    if y + 1 < m and island_sizes[y + 1][x][0] > 0 and island_sizes[y + 1][x][1] not in islands_added:
                        size += island_sizes[y + 1][x][0]

                    max_island_size = max(size, max_island_size)

        if max_island_size == 0:
            return m * n
        
        return max_island_size