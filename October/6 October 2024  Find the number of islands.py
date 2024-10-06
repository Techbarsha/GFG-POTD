class Solution:
    def numIslands(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            while stack:
                x, y = stack.pop()
                for dir in directions:
                    new_x, new_y = x + dir[0], y + dir[1]
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 0
                        stack.append((new_x, new_y))
        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island_count += 1
                    dfs(i, j)
        
        return island_count
