class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        if not mat or not mat[0]:
            return []

        # Initialize boundaries for the matrix
        top, bottom, left, right = 0, len(mat) - 1, 0, len(mat[0]) - 1
        result = []

        # Traverse the matrix in spiral order
        while top <= bottom and left <= right:
        
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            # Traverse from top to bottom on the right column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            # Traverse from right to left on the bottom row (if still valid)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            # Traverse from bottom to top on the left column (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
