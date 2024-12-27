class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        
        freq = {}
        count = 0
        
        for num in arr:
            complement = target - num
            
            if complement in freq:
                count += freq[complement]
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        
        return count
