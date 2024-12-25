class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])

        # Flags to determine if the first row and first column need to be zeroed
        first_row_zero = any(mat[0][j] == 0 for j in range(m))
        first_col_zero = any(mat[i][0] == 0 for i in range(n))

        # Use the first row and column as markers
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Set matrix cells to zero based on markers
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Update the first row and column if needed
        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0
        if first_col_zero:
            for i in range(n):
                mat[i][0] = 0
