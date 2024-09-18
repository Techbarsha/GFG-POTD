class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code edutech barsha
        stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}
        for char in x:
            if char in '({[':
                stack.append(char)
        
            elif char in ')}]':
                if not stack or stack[-1] != matching_brackets[char]:
                    return False
                stack.pop()
        return not stack
