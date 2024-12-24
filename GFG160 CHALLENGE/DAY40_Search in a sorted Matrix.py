class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here
    	
    	n = len(mat)
        m = len(mat[0])

        # Start binary search treating the 2D matrix as a 1D array
        low, high = 0, n * m - 1

        while low <= high:
            mid = (low + high) // 2
            
            # Convert mid index to 2D indices
            row = mid // m
            col = mid % m
            mid_element = mat[row][col]

            if mid_element == x:
                return True
                
            elif mid_element < x:
                low = mid + 1
            else:
                high = mid - 1

        return False
