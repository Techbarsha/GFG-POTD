'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        a = []
        def s(r):
            if not r:
                a.append(-1)
                return
            
            a.append(r.data)
            s(r.left)
            s(r.right)
        s(root)
        return a
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):
        #code here
        self.i = 0
        def d():
            if self.i >= len(arr) or arr[self.i] == -1:
                self.i += 1
                return None
                
            r = Node(arr[self.i])
            self.i += 1
            r.left = d()
            r.right = d()
            return r
            
        return d()    
