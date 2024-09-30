class Solution:
    def __init__(self):
        # This will store the previous node in the in-order traversal
        self.prev = None

    # Function to convert a binary tree to doubly linked list.
    def bToDLL(self, root):
        # Code edutech barsha
        # Base case: if the tree is empty
        if not root:
            return None
        head = None

        # Recursive in-order traversal function
        def inorder(curr):
            nonlocal head
            if not curr:
                return
            inorder(curr.left)

            # Now process the current node:
            if self.prev is None:
                # This means curr is the leftmost node, so it becomes head
                head = curr
            else:
                # Adjust the pointers for DLL
                curr.left = self.prev  # previous node becomes the left pointer
                self.prev.right = curr  # current node becomes the right of prev

            # Mark current node as previous for the next iteration
            self.prev = curr

            # Recursively traverse the right subtree
            inorder(curr.right)

        inorder(root)
        return head
