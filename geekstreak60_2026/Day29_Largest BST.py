class Solution:
    def largestBst(self, root):
        # Your code here
        # This code implemented by Barsha Saha
        self.maxSize = 0
        
        def dfs(node):
            # Base case
            if not node:
                return (True, 0, float('inf'), float('-inf'))
            
            left_isBST, left_size, left_min, left_max = dfs(node.left)
            right_isBST, right_size, right_min, right_max = dfs(node.right)
            
            # Check BST condition
            if left_isBST and right_isBST and left_max < node.data < right_min:
                size = left_size + right_size + 1
                self.maxSize = max(self.maxSize, size)
                return (
                    True,
                    size,
                    min(left_min, node.data),
                    max(right_max, node.data)
                )
            
            # Not a BST
            return (False, 0, float('-inf'), float('inf'))
        
        dfs(root)
        return self.maxSize
        
