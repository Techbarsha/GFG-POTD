class Solution:
    # Function to merge two sorted doubly linked lists.
    def merge(self, left, right):
        # If any of the lists is empty, return the other list
        if not left:
            return right
        if not right:
            return left

        # Compare the data of the nodes and merge accordingly
        if left.data < right.data:
            left.next = self.merge(left.next, right)
            left.next.prev = left
            left.prev = None
            return left
        else:
            right.next = self.merge(left, right.next)
            right.next.prev = right
            right.prev = None
            return right

    # Function to perform merge sort on a doubly linked list.
    def mergeSort(self, head):
        if not head or not head.next:
            return head

        # Find the middle of the list
        middle = self.getMiddle(head)
        next_to_middle = middle.next
        middle.next = None

        # Recursively sort the two halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_middle)

        # Merge the sorted halves
        sorted_list = self.merge(left, right)
        return sorted_list

    # Function to find the middle of a doubly linked list.
    def getMiddle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    
        
    def sortDoubly(self,head):
    #Your code here
     # Call merge sort on the list
        sorted_list = self.mergeSort(head)
        return sorted_list
