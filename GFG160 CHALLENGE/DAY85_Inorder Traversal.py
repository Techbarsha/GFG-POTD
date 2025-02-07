'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        l = []
        def rec(rt):
            if not rt:
                return
            rec(rt.left)
            l.append(rt.data)
            rec(rt.right)
            
        rec(root)
        return l
