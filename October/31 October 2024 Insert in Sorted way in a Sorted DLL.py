#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    
    def sortedInsert(self, head, x):    
        new_node = Node(x)
        if head is None or head.data >= x:
            new_node.next = head
            if head:
                head.prev = new_node
            return new_node          
        current = head
        while current.next and current.next.data < x:
            current = current.next

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

        return head 
