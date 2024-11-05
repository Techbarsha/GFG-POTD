def rotate(mat): 
    #code here
    n = len(mat)
    
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    for i in range(n):
        mat[i].reverse()
