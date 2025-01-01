class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        anagram_dict = {}
        
        for word in arr:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = []
                
            anagram_dict[sorted_word].append(word)
            
        return list(anagram_dict.values())    
