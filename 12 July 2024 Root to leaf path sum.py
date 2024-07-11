class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        # code here
        # if the tree is empty
        if root is None:
            return False
        
        # If it's a leaf node, check if the current path sum equals the target
        if root.left is None and root.right is None:
            return target == root.data
        
        # Recursive case: subtract the current node's value from the target
        # and check the left and right subtrees
        remaining_sum = target - root.data
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))
