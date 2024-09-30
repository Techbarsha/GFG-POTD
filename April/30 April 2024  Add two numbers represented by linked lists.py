class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head

        prev, temp, next_node = None, head, head.next
        while next_node:
            temp.next = prev
            prev = temp
            temp = next_node
            next_node = temp.next
        temp.next = prev

        return temp

    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1
        tail = None
        carry = 0

        while l1 and l2:
            l1.data += carry + l2.data
            carry = l1.data // 10
            l1.data %= 10

            tail = l1

            l1 = l1.next
            l2 = l2.next

        if l2:
            tail.next = l2
            l1 = l2

        while l1:
            l1.data += carry
            carry = l1.data // 10
            l1.data %= 10
            tail = l1
            l1 = l1.next

        l1 = tail
        while carry:
            l1.next = Node(carry)
            carry = l1.data // 10
            l1.data %= 10
            l1 = l1.next

        return head

    def addTwoLists(self, num1, num2):
        while num1.next and num1.data == 0:
            num1 = num1.next
        while num2.next and num2.data == 0:
            num2 = num2.next

        num1 = self.reverse(num1)
        num2 = self.reverse(num2)

        return self.reverse(self.addTwoNumbers(num1, num2))
