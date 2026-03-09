class Solution:
    def largestSwap(self, s):
        #code here
        # This code implemented by barsha saha
        arr = list(s)
        
        # store last occurrence of each digit
        last = {}
        for i, ch in enumerate(arr):
            last[ch] = i
        
        # try to swap
        for i in range(len(arr)):
            # check for bigger digits from 9 downwards
            for d in range(9, int(arr[i]), -1):
                if str(d) in last and last[str(d)] > i:
                    j = last[str(d)]
                    arr[i], arr[j] = arr[j], arr[i]
                    return "".join(arr)
        
        return s
        
