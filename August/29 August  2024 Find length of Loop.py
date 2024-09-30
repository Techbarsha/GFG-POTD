class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        # code edutech barsha
        if head is None:
            return 0
        
        slow = head
        fast = head
        
        # Step 1: Detect the loop using Floyd's Cycle-Finding Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Loop detected
            if slow == fast:
                # Step 2: Count the number of nodes in the loop
                count = 1
                current = slow.next
                while current != slow:
                    count += 1
                    current = current.next
                return count
        
        # No loop found
        return 0
