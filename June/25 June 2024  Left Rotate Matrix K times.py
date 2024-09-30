class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)
        m = len(mat[0])
        k = k % m  # Effective rotations
        result = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                new_position = (j + m - k) % m
                result[i][new_position] = mat[i][j]
        
        return result
