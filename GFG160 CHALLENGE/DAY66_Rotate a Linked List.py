class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        
        if k == 0 or head is None:
            return head
            
        curr = head
        lenn = 1
        
        while curr.next is not None:
            curr = curr.next
            lenn += 1
            
        k %= lenn
        
        if k == 0:
            curr.next = None
            return head
            
        curr.next = head
        curr = head
        
        for _ in range(1,k):
            curr = curr.next
            
        nhead = curr.next
        curr.next = None
        
        return nhead
