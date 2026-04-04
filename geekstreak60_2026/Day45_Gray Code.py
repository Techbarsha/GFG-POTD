class Solution:
    def graycode(self,n):
        #code here
        
        # This code implemented by Barsha Saha
        result = []
        for i in range(1 << n): 
            gray = i ^ (i >> 1)
            result.append(format(gray, f'0{n}b'))
        
        return result
        
        
