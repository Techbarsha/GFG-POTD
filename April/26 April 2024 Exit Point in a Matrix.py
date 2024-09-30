class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
		directions = [(0,1),(1,0),(0,-1),(-1,0)]
		
		x,y = 0,0
		direction_index = 0
		
		while True:
		   if x < 0 or x >= n or y < 0 or y >= m:
		    return [x - directions[direction_index][0], y - directions[direction_index][1]]
		    
		   if matrix[x][y] == 0:
		     x += directions[direction_index][0]
		     y += directions[direction_index][1]
		   else:
		     direction_index = (direction_index + 1) % 4
		     matrix[x][y] = 0
		     x += directions[direction_index][0]
		     y += directions[direction_index][1]
