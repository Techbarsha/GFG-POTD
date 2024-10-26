class Solution:
    def count(self, head, key):
        # Code here
        count = 0
        # Traverse the linked list
        current = head
        while current is not None:
            # If the current node's data matches the key, increment count
            if current.data == key:
                count += 1
            # Move to the next node
            current = current.next
        # Return the final count of occurrences
        return count
