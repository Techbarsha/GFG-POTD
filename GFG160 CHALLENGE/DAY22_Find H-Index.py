class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        
        citations.sort(reverse=True)
        h_index = 0
        
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index
