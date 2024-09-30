class Solution:
    def solveNQueens(self, n):
        # code edutech barsha
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True

        def solve(row, board):
            if row == n:
                result.append(board[:])
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    solve(row + 1, board)
                    board[row] = -1
        
        result = []
        solve(0, [-1] * n)
        
        # Format the result as required
        formatted_result = []
        for solution in result:
            formatted_result.append([x + 1 for x in solution])
        
        return formatted_result

    def nQueen(self, n):
        return self.solveNQueens(n)
