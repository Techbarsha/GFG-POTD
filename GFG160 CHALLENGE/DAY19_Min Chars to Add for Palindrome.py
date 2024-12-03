class Solution:
    def minChar(self, s):
        #Write your code here
        
        rev_s = s[::-1]
        concat = s + '#' + rev_s
        n = len(concat)
        lps = [0] * n
        
        for i in range(1, n):
            length = lps[i - 1]
            
            while length > 0 and concat[i] != concat[length]:
                length = lps[length - 1]
                
            if concat[i] == concat[length]:
                length += 1
                
            lps[i] = length
        
        return len(s) - lps[-1]
