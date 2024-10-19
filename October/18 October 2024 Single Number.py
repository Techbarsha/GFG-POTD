class Solution:
    
    def getSingle(self,arr):
        # code here
        number = 0
        
        for num in arr:
            number ^= num
        
        return number
