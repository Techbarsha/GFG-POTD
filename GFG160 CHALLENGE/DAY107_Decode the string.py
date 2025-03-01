class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        curr_str = ""
        num = 0
        for char in s:
            if char.isdigit():
                num=num*10+int(char)
            elif char == '[':
                stack.append((curr_str,num))
                curr_str = ""
                num = 0
            elif char == ']':
                prev_str,repeat = stack.pop()
                curr_str = prev_str + (curr_str * repeat)
            else:
                curr_str += char
                
        return curr_str  
