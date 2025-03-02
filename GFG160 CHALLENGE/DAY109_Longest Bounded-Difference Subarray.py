from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        left = 0 
        max_len = 0
        best_start = 0
        
        min_deque = deque()
        max_deque = deque()
        
        for right in range(len(arr)):
            while max_deque and arr[max_deque[-1]] < arr[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while min_deque and arr[min_deque[-1]] > arr[right]:
                min_deque.pop()
            min_deque.append(right)
            
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
                    
            if right - left + 1 > max_len:
                max_len = right - left + 1
                best_start = left
                
        return arr[best_start:best_start + max_len]        
