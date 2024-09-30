from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        # code here
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        # Helper function to check if a cell is within bounds
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < columns

        # Helper function to check if there exists a path with given max_diff
        def bfs(max_diff):
            queue = [(0, 0)]  # (x, y)
            visited = set()
            visited.add((0, 0))

            while queue:
                x, y = queue.pop(0)

                if x == rows - 1 and y == columns - 1:
                    return True  # Path found

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if is_valid(new_x, new_y) and (new_x, new_y) not in visited \
                            and abs(heights[x][y] - heights[new_x][new_y]) <= max_diff:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))

            return False  # No path found

        # Binary search for minimum effort
        left, right = 0, 10**6
        while left < right:
            mid = (left + right) // 2
            if bfs(mid):
                right = mid
            else:
                left = mid + 1

        return left
