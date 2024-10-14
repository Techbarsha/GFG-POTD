class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
