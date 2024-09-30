class Solution:
    def removeAllDuplicates(self, head):
        #code here
        dummy = Node(0)  # Create a dummy node to handle edge cases more easily
        dummy.next = head
        prev = dummy  # The last node before the sublist of duplicates
        current = head  # The current node we're examining
        
        while current:
            # Check if current node is a start of a duplicate sublist
            has_duplicates = False
            while current.next and current.data == current.next.data:
                has_duplicates = True
                current = current.next
            
            if has_duplicates:
                # Skip all duplicates
                prev.next = current.next
            else:
                # Move prev to current if no duplicate in sublist
                prev = prev.next
            
            # Move current to the next node
            current = current.next
        
        return dummy.next
