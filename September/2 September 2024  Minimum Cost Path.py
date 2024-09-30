import heapq

class Solution:
    # Function to return the minimum cost to reach the bottom-right cell from the top-left cell.
    def minimumCostPath(self, grid):
        n = len(grid)
        # Directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Priority queue to store the cells along with the cost to reach them
        pq = [(grid[0][0], 0, 0)]  # (cost, x, y)
        # 2D array to store the minimum cost to reach each cell
        min_cost = [[float('inf')] * n for _ in range(n)]
        min_cost[0][0] = grid[0][0]
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            # If we reach the bottom-right cell, return the cost
            if x == n - 1 and y == n - 1:
                return cost
            
            # Explore the four possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is within the grid bounds
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    
                    # If a new lower cost is found, update and push to the priority queue
                    if new_cost < min_cost[nx][ny]:
                        min_cost[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        
        return -1  # This line is unreachable as the grid is always solvable
