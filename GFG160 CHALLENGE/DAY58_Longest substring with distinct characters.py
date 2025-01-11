class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        
        char_map = {}
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
                
            char_map[s[end]] = end
            
            max_length = max(max_length, end - start + 1)
            
        return max_length    
