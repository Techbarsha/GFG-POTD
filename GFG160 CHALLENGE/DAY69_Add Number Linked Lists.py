#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        
        def reverseList(head):
            prev = None
            current = head
            
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                
            return prev
            
        num1 = reverseList(num1)
        num2 = reverseList(num2)
        carry = 0
        dummy = Node(0)
        current = dummy
        
        while num1 or num2 or carry:
            val1 = num1.data if num1 else 0
            val2 = num2.data if num2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = Node(total % 10)
            current = current.next
            
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
                
        result = reverseList(dummy.next)
        
        while result and result.data == 0:
            result = result.next
            
        return result if result else Node(0)
        
