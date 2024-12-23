class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x):
    	# code here 
    	
    	for i in range(len(mat)):
            if mat[i][-1]>0:
                for j in range(len(mat[i])):
                    if mat[i][j]==x:
                        return True
                        
        return False
