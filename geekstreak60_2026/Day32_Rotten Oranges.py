from collections import deque
class Solution:
	def orangesRot(self, mat):
		# code here
        # This code implemented by Barsha Saha
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        fresh = 0

        # Initialize queue and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    queue.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1

        # If no fresh oranges
        if fresh == 0:
            return 0
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        #  BFS
        while queue:
            size = len(queue)
            rotten_this_round = False
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                        mat[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
                        rotten_this_round = True

            if rotten_this_round:
                time += 1

        # Check if all fresh are rotten
        return time if fresh == 0 else -1
