class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        fast = slow = head
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both fast and slow until fast reaches the end of the list
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Now, slow is at the start of the last n nodes, calculate their sum
        total_sum = 0
        while slow:
            total_sum += slow.data
            slow = slow.next
        
        return total_sum
