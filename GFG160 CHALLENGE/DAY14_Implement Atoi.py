class Solution:
    def myAtoi(self, s):
        # Code here
        
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        start = 0
        
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        num = 0
        
        for i in range(start, len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            else:
                break
        
        num *= sign
        int_min = -2**31
        int_max = 2**31 - 1
        
        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        
        return num
