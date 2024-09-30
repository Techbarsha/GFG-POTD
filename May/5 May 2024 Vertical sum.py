class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        
        #code here
        vertical_sums = {}

        def vertical_traversal(node, hd):
            if node is None:
                return
           
            vertical_sums[hd] = vertical_sums.get(hd, 0) + node.data
            vertical_traversal(node.left, hd - 1)
            vertical_traversal(node.right, hd + 1)

        vertical_traversal(root, 0)
        sorted_sums = sorted(vertical_sums.items())
        return [sum_val for _, sum_val in sorted_sums]
