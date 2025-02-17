import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        return heapq.nsmallest(k,points,key=lambda p:p[0]**2+p[1]**2)
