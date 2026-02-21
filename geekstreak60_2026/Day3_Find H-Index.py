class Solution:
    def hIndex(self, citations):  
        #code here
        
        # this code implemented by barsha saha
        citations.sort(reverse=True)
        
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        
        return h
        
