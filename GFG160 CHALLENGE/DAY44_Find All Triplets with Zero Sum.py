class Solution:
    def findTriplets(self, arr):
        # Your code here
        
        ans=[]
        
        for i in range(0,len(arr)):
            d={}
            
            for j in range(i+1,len(arr)):
                if -(arr[i]+arr[j]) in d:
                    for num in d[-(arr[i]+arr[j])]:
                        ans.append([i,num,j])
                        
                if arr[j] in d:
                    d[arr[j]].append(j)
                else:
                    d[arr[j]]=[j]
        return ans
