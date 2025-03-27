class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        count=0
        maxi=-1
        i=0
        j=0
        n=len(arr)
        while i < n and j < n:
            if arr[i] <= dep[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            maxi=max(maxi,count)
        maxi=max(maxi,count)
        return maxi
