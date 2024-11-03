class Solution:
    def isLengthEven(self, head):
        output=True
        if not head:
            return output
        temp=head
        while temp:
            temp=temp.next
            if output:
                output=False
            else:
                output=True
        return output
