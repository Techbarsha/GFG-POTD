import heapq

class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        
class Solution:
    def sortAKSortedDLL(self, head, k):
        # Code Here
        minHeap = []
        temp1 = head
        temp2 = head
        
        while temp1:
            heapq.heappush(minHeap, temp1.data)
            
            if len(minHeap) == k + 1:
                temp2.data = heapq.heappop(minHeap)
                temp2 = temp2.next
            
            temp1 = temp1.next
        
        while minHeap:
            temp2.data = heapq.heappop(minHeap)
            temp2 = temp2.next
        
        return head
