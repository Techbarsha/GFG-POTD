class Solution:
    def RemoveHalfNodes(self, node):
        #code here
        if not node:
            return None
            
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        if node.left and not node.right:
           return node.left
           
        if not node.left and node.right:
           return node.right
           
        return node 
