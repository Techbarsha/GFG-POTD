class Solution:
    def alternatingSplitList(self, head):
        # code here
        if not head:  # If the list is empty, return two empty lists
            return [None, None]
        
        # Initialize pointers for both lists
        head1 = tail1 = None  # List 1 (even indexed nodes)
        head2 = tail2 = None  # List 2 (odd indexed nodes)
        
        flag = True  # To alternate between the two lists
        current = head
        
        while current:
            if flag:
                if not head1:
                    head1 = tail1 = current
                else:
                    tail1.next = current
                    tail1 = tail1.next
            else:
                if not head2:
                    head2 = tail2 = current
                else:
                    tail2.next = current
                    tail2 = tail2.next
            
            current = current.next
            flag = not flag  # Alternate the flag
        
        # Terminate the two lists
        if tail1:
            tail1.next = None
        if tail2:
            tail2.next = None
        
        return [head1, head2]
