# Tree Node structure
class Tree:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to make binary tree from linked list.
def convert(head):
    # code here
    if not head:
        return None

    # Create the root of the tree
    root = Tree(head.data)
    queue = [root]
    
    current = head.next
    while current:
        # Pop the current node from the front of the queue
        parent = queue.pop(0)
        
        # Take the next node from the linked list and make it the left child of the current parent node
        leftChild = Tree(current.data)
        parent.left = leftChild
        queue.append(leftChild)
        
        # Move to the next node
        current = current.next
        if current:
            # Take the next node from the linked list and make it the right child of the current parent node
            rightChild = Tree(current.data)
            parent.right = rightChild
            queue.append(rightChild)
            
            # Move to the next node
            current = current.next

    return root

# Class to convert the linked list to Binary Tree
class Conversion:
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self):
        self.head = None
        self.root = None

    def push(self, new_data):
        # Creating a new linked list node and storing data
        new_node = ListNode(new_data)
        # Make next of new node as head
        new_node.next = self.head
        # Move the head to point to new node
        self.head = new_node

    def levelorderTraversal(self, root):
        if root is None:
            return

        # Perform level order traversal using a queue
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Print the level order traversal
        print(*result)

# Linked List node
class ListNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
