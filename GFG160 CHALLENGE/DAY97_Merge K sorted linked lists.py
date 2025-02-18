'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
import heapq
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        pq = []
        for i, head in enumerate(arr):
            if head:
                heapq.heappush(pq, (head.data, i, head.next))
                
        dummyNode = Node(-1)
        curr = dummyNode
        
        while pq:
            val, ind,  head = heapq.heappop(pq)
            curr.next = Node(val)
            curr = curr.next
            
            if head:
                heapq.heappush(pq, (head.data, ind, head.next))
                
        return dummyNode.next
