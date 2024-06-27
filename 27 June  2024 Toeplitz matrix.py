def isToeplitz(mat):
    #code here
    rows = len(mat)
    cols = len(mat[0])
    
    # Iterate through each element in the matrix
    for row in range(rows):
        for col in range(cols):
        # Check if there is an element in the diagonal below-right
            if row + 1 < rows and col + 1 < cols:
  # Compare current element with the element in nxt diagonal position
                if mat[row][col] != mat[row + 1][col + 1]:
        # If any diagonal elements do not match, return False
                    return False
    
    # If all diagonals are consistent, return True
    return True
