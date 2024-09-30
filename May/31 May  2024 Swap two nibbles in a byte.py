class Solution:
    def swapNibbles (self, n):
        # code here 
        # Isolate and swap the nibbles, then combine them
        #0x0F: In binary, this is 00001111
        #0xF0: In binary, this is 11110000
        return ((n & 0x0F) << 4) | ((n & 0xF0) >> 4)
