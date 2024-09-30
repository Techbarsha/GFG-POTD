class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        paths = []

        def find_paths(node, current_path):
            if not node:
                return
            # Append the current node's value to the current path
            current_path.append(node.data)

            # If the current node is a leaf node, add the current path to the paths list
            if not node.left and not node.right:
                paths.append(list(current_path))
            else:
                # Recursively find paths for left and right subtrees
                find_paths(node.left, current_path)
                find_paths(node.right, current_path)

            # Backtrack: Remove the current node from the current path
            current_path.pop()

        find_paths(root, [])
        return paths
