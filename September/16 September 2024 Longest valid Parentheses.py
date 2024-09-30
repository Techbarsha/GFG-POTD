class Solution:
    def maxLength(self, str):
        # code edutech barsha
        stack = [-1]
        max_len = 0

        for i in range(len(str)):
            if str[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
