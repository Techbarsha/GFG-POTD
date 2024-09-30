class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code edutech barsha
        if root is None:
            return
        
        root.left, root.right = root.right, root.left
        
       
        self.mirror(root.left)
        self.mirror(root.right)
