#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        dic={}
        i=0;j=0;n=len(arr)
        while j<n:
            dic[arr[j]]=dic.get(arr[j],0)+1
            #print(dic)
            if (j-i)==k:
                if len(dic)<(j-i)+1:
                    return True
                dic[arr[i]]-=1
                if dic[arr[i]]==0:
                    del dic[arr[i]]
                i+=1
            j+=1
        return False
