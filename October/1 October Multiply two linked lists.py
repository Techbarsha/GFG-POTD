class Solution:
    MOD = 10**9 + 7 
    def multiply_two_lists(self, first, second):
        # Code here
        num1 = 0
        while first:
            num1 = (num1 * 10 + first.data) % self.MOD
            first = first.next
        num2 = 0
        while second:
            num2 = (num2 * 10 + second.data) % self.MOD
            second = second.next
        
        return (num1 * num2) % self.MOD
