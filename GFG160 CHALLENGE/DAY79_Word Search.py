class Solution:
	def isWordExist(self, mat, word):
		#Code here
	   def dfs(i, j, k):
		    if k == len(word):
		        return True
		    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or mat[i][j] != work[k]:
		        return False
		    temp, mat[i][j] = mat[i][j], '#'
		    found = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
		    mat[i][j] = temp
		    return found
		    
		for i in range(len(mat)):
		    for j in range(len(mat[0])):
		       if mat[i][j] == word[0] and dfs(i, j, 0):
		          return True
		return False
