class Solution:
    def evaluate(self, arr):
        # code here
        stack=[]
        for i in arr:
            if i=='+' or i=='-' or i=='/' or i=='*':
                b=stack.pop()
                a=stack.pop()
                if i == '+':
                    stack.append(int(a)+int(b))
                elif i == '-':
                    stack.append(int(a)-int(b))
                elif i == '*':
                    stack.append(int(a)*int(b))    
                elif i == '/':
                    stack.append(int(int(a) / int(b)))
            else:
                stack.append(i)
        return stack.pop()
