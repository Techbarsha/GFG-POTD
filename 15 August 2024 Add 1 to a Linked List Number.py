# code edutech barsha
class Solution:
    def reverse(self, head):
        # Reverse the linked list
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def addOne(self, head):
        #Returns new head of linked List.
        # Reverse the list to process from the least significant digit
        head = self.reverse(head)
        
        # Add 1 to the number represented by the linked list
        carry = 1
        current = head
        
        while current:
            sum_value = current.data + carry
            current.data = sum_value % 10
            carry = sum_value // 10
            
            # If carry remains and it's the last node, add a new node
            if carry and current.next is None:
                current.next = Node(0)
            current = current.next
        
        # Reverse the list back to original order
        head = self.reverse(head)
        
        return head
