class Solution:
    def longestCommonPrefix(self, arr):
        # code here edutech barsha
        if not arr:
            return "-1"
            
        min_length = min(len(s) for s in arr)
        
        if min_length == 0:
            return "-1"
            
        prefix = ""
        
        for i in range(min_length):
            current_char = arr[0][i]
            
            for string in arr:
                if string[i] != current_char:
                    return prefix if prefix else "-1"
            
           
            prefix += current_char
        
        return prefix if prefix else "-1"
 
