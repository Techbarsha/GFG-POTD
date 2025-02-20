import heapq
class Solution:
    def getMedian(self, arr):
        
        ret,up,dn = [],[],[]
        
        for ve in arr:
            ve = heapq.heappushpop(up,ve)
            ve = - heapq.heappushpop(dn,-ve)
            if len(up) == len(dn):
                ret.append(ve)
                heapq.heappush(up,ve)
            elif len(up)>len(dn):
                ret.append((up[0]+ve)/2)
                heapq.heappush(dn,-ve)
            else:
                ret.append((-dn[0]+ve)/2)
                heapq.heappush(up,ve)
        return ret   
