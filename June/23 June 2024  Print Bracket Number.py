class Solution:
	def bracketNumbers(self, str):
		# code here
		stack = []
        result = []
        bracket_number = 1

        for char in str:
            if char == '(':
                stack.append(bracket_number)
                result.append(bracket_number)
                bracket_number += 1
            elif char == ')':
                result.append(stack.pop())
            # Skip adding non-bracket characters to result
            # else:
            #     result.append(-1)

        return result
