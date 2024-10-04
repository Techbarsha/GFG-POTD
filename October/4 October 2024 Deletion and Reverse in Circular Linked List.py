class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        #code here
        if head is None or head.next == head:
            return head  
        
        prev = None
        current = head
        next_node = None
        first = head  

        while True:
            next_node = current.next  
            current.next = prev  
            prev = current  
            current = next_node  
            if current == head:
                break  
        head.next = prev  
        return prev
        
    def deleteNode(self, head, key):
        #code here
        if head is None:
            return None
        
        if head.data == key:
            if head.next == head:
                return None
                
            last = head
            while last.next != head:
                last = last.next
            
            last.next = head.next
            head = head.next  
            return head
        
        current = head
        while current.next != head:
            if current.next.data == key:
                
                current.next = current.next.next
                return head
            current = current.next
        
        return head
