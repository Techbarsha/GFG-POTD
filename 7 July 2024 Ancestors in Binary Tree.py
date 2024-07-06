class Solution:

    def Ancestors(self, root, target):
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        #code here
         # Helper function to perform DFS and find the ancestors
        def find_ancestors(node, target, path):
            if not node:
                return False
            # Add current node to path
            path.append(node.data)
            # If current node is the target, return True
            if node.data == target:
                return True
            # Recur for left and right subtree
            if (find_ancestors(node.left, target, path) or 
                find_ancestors(node.right, target, path)):
                return True
            # If not found in either left or right subtree, backtrack
            path.pop()
            return False
        
        # List to store the path (ancestors)
        path = []
        # Call the helper function with the initial path
        find_ancestors(root, target, path)
        # Since the target itself will be included, we remove it
        if path and path[-1] == target:
            path.pop()
        # The ancestors should be in reverse order
        path.reverse()
        return path
