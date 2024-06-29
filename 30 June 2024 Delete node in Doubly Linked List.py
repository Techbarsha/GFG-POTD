class Solution:
    def delete_node(self, head, x):
        #code here
        # If the list is empty
        if not head:
            return None
        
        # If we need to delete the head node
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        
        # Traverse to the node to be deleted
        current = head
        for _ in range(x - 1):
            if current:
                current = current.next
        
        # If the node to be deleted is found
        if current:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        
        return head
