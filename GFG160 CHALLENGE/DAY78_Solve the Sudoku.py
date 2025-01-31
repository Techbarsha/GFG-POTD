#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        # Your code here
        def is_valid(mat, row, col, num):
            for i in range(9):
                if mat[row][i] == num or mat[i][col] == num:
                    return False
            
            start_row, start_col = 3 * (row // 3), 3 *(col // 3)
            for i in range(3):
                for j in range(3):
                    if mat[start_row + i][start_col + j] == num:
                        return False
            return True
            
        def solve():
            for row in range(9):
                for col in range(9):
                    if mat[row][col] == 0:
                        for num in range(1, 10):
                            if is_valid(mat, row, col, num):
                                mat[row][col] = num
                                if solve():
                                    return True
                                mat[row][col] = 0
                        return False
            
            return True
            
        solve() 
