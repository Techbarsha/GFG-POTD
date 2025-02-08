#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):
        # Code here
        if not root:
            return []
        result = []
        if root.left or root.right:
            result.append(root.data)
            
        self.getLeftBoundary(root.left,result) 
        self.getLeafNodes(root,result)
        
        right_boundary = []
        self.getRightBoundary(root.right,right_boundary)
        result.extend(reversed(right_boundary))
        
        return result
        
    def getLeftBoundary(self,node,result):
        while node:
            if node.left or node.right:
                result.append(node.data)
            if node.left:
                node = node.left
            else:
                node = node.right
                
    def getLeafNodes(self,node,result):
        if not node:
            return
        if not node.left and not node.right:
            result.append(node.data)
            return
        self.getLeafNodes(node.left,result)
        self.getLeafNodes(node.right,result)
        
    def getRightBoundary(self,node,result):
        while node:
            if node.left or node.right:
                result.append(node.data)
            if node.right:
                node = node.right
            else:
                node = node.left
