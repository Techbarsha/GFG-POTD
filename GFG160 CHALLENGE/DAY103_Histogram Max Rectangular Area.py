class Solution:
    def getMaxArea(self,arr):
        #code here
        mx = 0
        stk = []
        for ix,ve in enumerate(arr):
            while stk and arr[stk[-1]] >= ve:
                stk.pop()
            stk.append(ix)
            for j,ve in enumerate(stk):
                if j==0:
                    mx=max(mx,arr[stk[j]]*(ix+1))
                    continue
                mx=max(mx,(arr[stk[j]])*(ix-stk[j-1]))
        return mx
