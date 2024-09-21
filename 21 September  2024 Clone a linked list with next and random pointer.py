class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code eedutech barsha
        if not head:
            return None
        
        curr = head
        while curr:
            new_node = Node(curr.data)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
       
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
      
        original = head
        copy = head.next
        new_head = head.next
        
        while original and copy:
            original.next = original.next.next
            copy.next = copy.next.next if copy.next else None
            original = original.next
            copy = copy.next
        
        return new_head
