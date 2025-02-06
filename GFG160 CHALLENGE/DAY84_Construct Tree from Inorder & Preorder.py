class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        index_map = { inorder[i] : i for i in range(len(inorder)) }
        pre_inx = 0
        def construct(left, right):
            nonlocal  pre_inx
            if left > right:
                return None
                
            val = preorder[pre_inx]
            pre_inx += 1
            inorder_inx = index_map[val]
            root = Node(val)
            root.left = construct(left, inorder_inx - 1)
            root.right = construct(inorder_inx + 1, right)
            
            return root
            
        return construct(0,len(inorder) - 1) 
