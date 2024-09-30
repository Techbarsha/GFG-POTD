class Solution:
    def isPalindrome(self, head):
        #code edutech barsha
        if head is None or head.next is None:
            return True
        def reverse(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        def find_middle(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
            
        middle = find_middle(head)
        second_half_start = reverse(middle)
        first_half = head
        second_half = second_half_start
        
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        reverse(second_half_start)
        return True
