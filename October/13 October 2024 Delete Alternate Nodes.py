class Solution:
    def deleteAlt(self, head):
        # code here
        if head is None or head.next is None:
            return head
        
        current = head
        
        while current is not None and current.next is not None:
            current.next = current.next.next
            current = current.next
            
        return head
