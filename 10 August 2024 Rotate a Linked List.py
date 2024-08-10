class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code edutech barsha
        if not head:
            return None
        
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = head
      
        while k - 1:
            head = head.next
            k -= 1
         new_head = head.next
        
        head.next = None
        
        return new_head
