#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
     # Traverse both lists
    while head1 is not None and head2 is not None:
        # If data of both nodes is not equal, return False
        if head1.data != head2.data:
            return False
        
        # Move to the next node in both lists
        head1 = head1.next
        head2 = head2.next
    
    # Check if either of the lists has nodes left
    if head1 is not None or head2 is not None:
        return False
    
    # If we reach here, both lists are identical
    return True
