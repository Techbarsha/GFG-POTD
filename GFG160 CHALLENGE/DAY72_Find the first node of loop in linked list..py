#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    def findFirstNode(self, head):
        #code here
        
        slow,fast = head,head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                 break
             
        if slow != fast:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
            
        return head    
