from heapq import heappush,heappop
class Solution:
    def jobSequencing(self, d, p):
        # code here
        jobs = sorted(zip(d,p))
        pq=[]
        for deadline,profit in jobs:
            if len(pq)<deadline:
                heappush(pq,profit)
            elif pq and pq[0] < profit:
                heappop(pq)
                heappush(pq,profit)
        return [len(pq),sum(pq)]        
        
