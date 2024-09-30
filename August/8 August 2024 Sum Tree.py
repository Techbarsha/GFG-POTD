class Solution:
    def is_sum_tree_helper(self, node):
        # Base case: An empty tree is a sum tree
        if node is None:
            return True, 0
        
        # Base case: A leaf node is a sum tree
        if node.left is None and node.right is None:
            return True, node.data
        
        # Recursive case: Check left and right subtrees
        left_is_sum_tree, left_sum = self.is_sum_tree_helper(node.left)
        right_is_sum_tree, right_sum = self.is_sum_tree_helper(node.right)
        
        # Check current node sum tree property
        current_is_sum_tree = (node.data == left_sum + right_sum)
        
        # Return the result for current node
        return (left_is_sum_tree and right_is_sum_tree and current_is_sum_tree), left_sum + right_sum + node.data
    
    def is_sum_tree(self, node):
        # code edutech barsha
        is_sum_tree, _ = self.is_sum_tree_helper(node)
        return is_sum_tree

# Utility function to create a new Tree Node
def new_node(val):
    return Node(val)

# Function to Build Tree
def build_tree(s):
    if not s or s[0] == 'N':
        return None

    ip = s.split()
    root = new_node(int(ip[0]))

    queue = []
    queue.append(root)

    i = 1
    while queue and i < len(ip):
        curr_node = queue.pop(0)
        curr_val = ip[i]

        if curr_val != "N":
            curr_node.left = new_node(int(curr_val))
            queue.append(curr_node.left)

        i += 1
        if i >= len(ip):
            break
        curr_val = ip[i]

        if curr_val != "N":
            curr_node.right = new_node(int(curr_val))
            queue.append(curr_node.right)
        i += 1

    return root
