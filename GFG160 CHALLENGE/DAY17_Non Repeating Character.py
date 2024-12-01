class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for char in s:
            if char_count[char] == 1:
                return char
        
        return '$'
