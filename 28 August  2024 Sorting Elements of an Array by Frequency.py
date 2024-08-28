from collections import Counter
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code edutech barsha
        freq = Counter(arr)
        
        sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
        
        return sorted_arr
