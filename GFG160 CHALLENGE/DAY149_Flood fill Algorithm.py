class Solution:
	def floodFill(self, A, sr, sc, nc):
		#Code here
		m,n,oc = len(A),len(A[0]),A[sr][sc]
		if oc == nc: return A
		q=[(sr,sc)]
		A[sr][sc]=nc
		d=[-1,0,1,0,-1]
		while q:
		    x,y = q.pop(0)
		    for i in range(4):
		        nx,ny = x + d[i], y + d[i+1]
		        if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == oc:
		            A[nx][ny]=nc
		            q.append((nx,ny))
	    return A  
