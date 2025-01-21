"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        l = []
        i = 0
        t = []
        while head:
            t.append(head.data)
            head = head.next
            i += 1
            if i == k or not head:
                l.append(t)
                t = []
                i = 0
        n = []
        for i in range(len(l)):
            n.extend(reversed(l[i]))
            
        new = Node(n[0])
        current = new
        for i in range(1,len(n)):
            t = Node(n[i])
            current.next = t
            current = current.next
            
        return new    
