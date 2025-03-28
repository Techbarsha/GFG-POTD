class Solution:
    def activitySelection(self, start, finish):
        #code here
        n=len(start)
        z=[[i,j] for i,j in zip(start,finish)]
        z.sort(key=lambda x:x[-1])
        r=0
        prev=0
        
        for x in range(1,n):
            if z[x][0]<=z[prev][1]:
                r+=1
                continue
            else:
                prev=x
                
        return n-r
