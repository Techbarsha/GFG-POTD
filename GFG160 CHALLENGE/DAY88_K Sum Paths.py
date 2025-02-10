'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def sumK(self,root,k):
        # code here
        count = [0]
        preSum = {}
        preSum[0] = 1
        
        self.rec(root,k,preSum,0,count)
        return count[0]
        
    def rec(self,node,k,preSum,s,count):
        if not node:
            return
        
        s += node.data
        diff = s-k
        
        count[0] += preSum.get(diff,0)
        preSum[s] = preSum.get(s,0)+1
        
        self.rec(node.left,k,preSum,s,count)
        self.rec(node.right,k,preSum,s,count)
        
        preSum[s] -= 1
        if preSum[s] == 0:
            preSum.pop(s)
            
        s -= node.data   
