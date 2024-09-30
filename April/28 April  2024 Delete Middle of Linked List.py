class Solution:
    def deleteMid(self, head):
        if not head or not head.next:
            return None  # Return None if the linked list is empty or has a single node

        slow = head  # Initialize slow pointer
        fast = head  # Initialize fast pointer
        prev = None  # Initialize previous pointer to keep track of the node before the middle node

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # At this point, slow is at the middle node, and prev is at the node before the middle node
        if prev:  # If prev is not None, it means there is more than one node in the linked list
            prev.next = slow.next  # Skip the middle node by updating the previous node's next pointer
        else:  # If prev is None, it means there is only one node in the linked list
            head = head.next  # Update the head to the next node (deleting the single node)

        return head  # Return the head of the modified linked list
