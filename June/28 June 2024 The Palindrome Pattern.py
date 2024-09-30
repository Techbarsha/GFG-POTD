class Solution:
     def pattern(self, arr):
         # code here
        n = len(arr)

        # Helper function to check if a list is a palindrome
        def is_palindrome(lst):
            return lst == lst[::-1]
        
        # Check all rows first
        for i in range(n):
            if is_palindrome(arr[i]):
                return "{} R".format(i)
        
        # Check all columns if no row is a palindrome
        for j in range(n):
            column = [arr[i][j] for i in range(n)]
            if is_palindrome(column):
                return "{} C".format(j)
        
        # If no palindromes found
        return "-1"
