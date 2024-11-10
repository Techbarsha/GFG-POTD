# Your task is to complete this function
# function should return max sum level in the tree
class Solution:
    def treePathSum(self,root):
        # Code here
        def calculate_path_sum(node, current_sum):
            # If node is None, there's nothing to add
            if not node:
                return 0
            
            # Update the current sum to include this node's value
            current_sum = current_sum * 10 + node.data
            
            # If it's a leaf node, return the current sum
            if not node.left and not node.right:
                return current_sum
            
            # Recursively calculate the sum for left and right subtrees
            left_sum = calculate_path_sum(node.left, current_sum)
            right_sum = calculate_path_sum(node.right, current_sum)
            
            # Return the total sum of all paths from root to leaf
            return left_sum + right_sum
        
        # Initialize the recursive traversal from the root node
        return calculate_path_sum(root, 0)
