#function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def reverseList(self, head):
        # Code here
        prev = None
        tmp = head
        
        while tmp:
            x = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = x
            
        return prev  
