#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        def is_safe(board,row,col):
            for i in range(col):
                if board[i] == row or \
                   board[i] - i == row - col or \
                   board[i] + i == row + col:
                       return False
            return True
            
        def solve(col,board):
            if col == n:
                result.append(board[:])
                return
            
            for row in range(1, n + 1):
                if is_safe(board,row,col):
                    board[col] = row
                    solve(col + 1,board)
                    board[col] = 0
                    
        result = []
        solve(0,[0] * n)
        return result
