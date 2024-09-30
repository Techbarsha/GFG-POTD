class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        if n < 3 or m < 3:
            return -1
            
        max_sum = float('-inf') # initialize max_sum to neg infinty
        for i in range(n-2):
            for j in range(m-2):
                hourglass_sum = (
                    mat[i][j] + mat[i][j + 1] + mat[i][j + 2] +
                    mat[i + 1][j + 1] +
                    mat[i + 2][j] + mat[i + 2][j + 1] + mat[i + 2][j + 2]
                )
                max_sum = max(max_sum, hourglass_sum)  # Update max_sum if needed
        
        if max_sum == float('-inf'):
            return -1
        else:
            return max_sum
