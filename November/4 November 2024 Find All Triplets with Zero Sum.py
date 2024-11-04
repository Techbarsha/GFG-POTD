#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        arr = [(arr[i],i) for i in range(n)]
        arr.sort()
        ans = []
        for i in range(n-2):
            j,k = i+1,n-1
            while j < k:
                if arr[i][0] + arr[j][0] + arr[k][0] == 0:
                    ans.append(list(sorted([arr[i][1],arr[j][1],arr[k][1]])))
                    #The other option of considering the j++ 
                    for u in range(j+1,k):
                        if arr[i][0] + arr[u][0] + arr[k][0] == 0:
                            ans.append(list(sorted([arr[i][1],arr[u][1],arr[k][1]])))
                    k -= 1
                elif arr[i][0] + arr[j][0] + arr[k][0] > 0:
                    k -= 1
                else:
                    j += 1
        return ans

        
