class Solution:

    def kthSmallest(self, arr,k):
        # code edutech barsha
        s =0
        unique_elements = set()
        for i in arr:
             unique_elements.add(i)
        i = 0
        while k > 0:
            if i in unique_elements:
                k -= 1
            i+=1
            
        return i-1    
