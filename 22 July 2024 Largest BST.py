class Solution:
    def largestBst(self, root):
        # code edutechbarsha
        # Helper function to perform the necessary checks and return relevant info
        def helper(node):
             # Base case: empty subtree
            if not node:
               return True,0,float('inf'),float('-inf'),0
       
            
            # Recursively get info from left and right subtrees
            l_is_bst,l_size,l_min,l_max,l_largest_bst = helper(node.left)
            r_is_bst,r_size,r_min,r_max,r_largest_bst = helper(node.right)
            
            # Check if current node is BST
            if l_is_bst and r_is_bst and l_max < node.data < r_min:
                # Current node is BST
                size = l_size + r_size + 1
                return True,size,min(node.data, l_min), max(node.data, r_max),max(size,l_largest_bst,r_largest_bst)
            else:    
                # Current node is not BST
                return False,0,0,0, max(l_largest_bst, r_largest_bst)
                
        
        # Get the result from the helper function
        _,_,_,_, largest_bst_size = helper(root)
        return largest_bst_size
