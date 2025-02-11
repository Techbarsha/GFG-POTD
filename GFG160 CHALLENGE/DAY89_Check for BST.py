class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def is_valid_bst(node,low,high):
            if not node:
                return True
            if node.data <= low or node.data >= high:
                return False
            return is_valid_bst(node.left, low, node.data) and is_valid_bst(node.right, node.data, high)
            
        return is_valid_bst(root, float('-inf'), float('inf')) 
