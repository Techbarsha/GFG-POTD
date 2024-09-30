class Solution:
    def populateNext(self, root):
        if not root:
            return
        
        # Initialize an empty stack and a pointer for the current node
        stack = []
        current = root
        prev = None  # Previous node in the in-order traversal

        while stack or current:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current is now the leftmost node
            current = stack.pop()
            
            # If there was a previous node, set its next pointer to current
            if prev:
                prev.next = current
            
            # Update prev to current
            prev = current
            
            # Visit the right subtree
            current = current.right
