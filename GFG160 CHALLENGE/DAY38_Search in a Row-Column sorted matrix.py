class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		
		# Number of rows
		n = len(mat)   
		# Number of columns
        m = len(mat[0]) 
        
        # Start from the top-right corner
        row, col = 0, m - 1
        
        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
                
            elif mat[row][col] > x:
                # Move left
                col -= 1  
            else:
                # Move down
                row += 1  
        
        return False
