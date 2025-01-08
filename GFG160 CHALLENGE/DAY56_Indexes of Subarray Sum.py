#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        
        sum = 0
        
        for i in range(0, len(arr)):
            sum = 0
            
            for j in range(i, len(arr)):
                sum += arr[j]
                
                if(sum == target):
                    return i+1,j+1
                    
                elif(sum > target):
                    break
                
                
        return (-1,)     
