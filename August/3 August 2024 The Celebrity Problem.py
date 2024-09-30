class Solution:
    def celebrity(self, mat):
        # code edutechbarsha
        n = len(mat)
        i, j = 0, n - 1
        
        # Identify the potential celebrity
        while i < j:
            if mat[i][j] == 1:
                # i knows j, i cannot be a celebrity
                i += 1
            else:
                # i does not know j, j cannot be a celebrity
                j -= 1
                
        # Now, i should be the potential celebrity
        candidate = i
        
        # Verify the potential celebrity
        for k in range(n):
            if k != candidate:
                if mat[candidate][k] == 1 or mat[k][candidate] == 0:
                    return -1
        
        return candidate
