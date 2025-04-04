class Solution:
	def isCycle(self, V, edges):
		#Code here
		p=[e for e in range(V+1)]
		def find(v):
		    if p[v]!= v:
		        p[v]=find(p[v])
		    return p[v]
		for u,v in edges:
		    r1=find(u)
		    r2=find(v)
		    if r1 == r2:
		        return True
		    p[r1]=r2
	    return false
