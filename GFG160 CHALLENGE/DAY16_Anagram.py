from collections import Counter

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        
        if len(s1) != len(s2):
            
            return False
        
        count_s1 = Counter(s1)
        count_s2 = Counter(s2)
        
        return count_s1 == count_s2
