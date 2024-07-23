class Solution:
    def merge(self, root1, root2):
        # code here edutechbarsha
        def inorder_traversal(root):
            stack, result = [], []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                result.append(root.data)
                root = root.right
            return result
        
        # Perform in-order traversal on both BSTs to get sorted lists
        list1 = inorder_traversal(root1)
        list2 = inorder_traversal(root2)
        
        
        combined_list = list1 + list2
        
        # Sort the combined list
        combined_list.sort()
        
        return combined_list
