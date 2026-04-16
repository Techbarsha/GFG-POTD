class Solution:
    def myAtoi(self, s):
        # code here
        # This code implemented by Barsha Saha
        i = 0
        n = len(s)
        
        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if string is empty after removing spaces
        if i == n:
            return 0
        
        #Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Convert digits to number
        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num
