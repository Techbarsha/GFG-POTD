#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        temp = Node(0)
        node = temp
        
        while head1 and head2:
            if head1.data <= head2.data:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            
            node = node.next
            
        node.next = head1 or head2
        
        return temp.next
