# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here
        hashMap = {}
        hashMap[None] = None
        old = head
        while old:
            hashMap[old] = Node(old.data)
            old = old.next
        old = head
        while old:
            newNode = hashMap[old]
            newNext = hashMap[old.next]
            newRandom = hashMap[old.random]
            newNode.next = newNext
            newNode.random = newRandom
            old = old.next
            
        return hashMap[head]
