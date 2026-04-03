class Solution:
    def diagView(self, mat):
        #code here.
        
        # This code implemented by Barsha Saha
        
        n = len(mat)
        result = []

        # Traverse all diagonals using sum of indices
        for s in range(2 * n - 1):
            for i in range(n):
                j = s - i
                if 0 <= j < n:
                    result.append(mat[i][j])

        return result
        
        
