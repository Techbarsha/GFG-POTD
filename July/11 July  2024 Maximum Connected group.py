from typing import List, Tuple

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
#code here
        n = len(grid)
        
        def dfs(i: int, j: int, component_id: int):
            stack = [(i, j)]
            visited.add((i, j))
            size = 0
            while stack:
                x, y = stack.pop()
                grid_id[x][y] = component_id
                size += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
            return size
        
        visited = set()
        grid_id = [[-1] * n for _ in range(n)]
        component_size = []
        component_id = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    size = dfs(i, j, component_id)
                    component_size.append(size)
                    component_id += 1
        
        max_size = max(component_size) if component_size else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    adjacent_components = set()
                    potential_size = 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            comp_id = grid_id[nx][ny]
                            if comp_id not in adjacent_components:
                                adjacent_components.add(comp_id)
                                potential_size += component_size[comp_id]
                    max_size = max(max_size, potential_size)
        
        return max_size
        

