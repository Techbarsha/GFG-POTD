import heapq
from typing import List
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
    
        # code edutech barsha
        heap = []
        for i in arr:
            heapq.heappush(heap,i)
        s = 0
        while(len(heap)>1):
            
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            s += x + y
            heapq.heappush(heap,x+y)
            
        return s
