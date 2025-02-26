class Solution:
    def maxOfMins(self, arr):
       # code here
       n = len(arr)
       res,l,s = [0]*n,[0]*n,[]
       for i in range(n+1):
           while s and (i == n or arr[s[-1]]>=arr[i]):
               j=s.pop()
               l[j]= i if not s else i-s[-1]-1
           if i<n:
               s.append(i)
       for i in range(n):
           res[l[i]-1]= max(res[l[i]-1],arr[i])
       for i in range(n-2,-1,-1):     
           res[i]=max(res[i],res[i+1])
       return res  
