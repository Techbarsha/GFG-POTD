class Solution:
	def binaryNextNumber(self, s):
		# code here
		s = list(s)  # Convert string to list for mutability
        c = '1'
        s.reverse()  # Reverse the string
        
        for i in range(len(s)):
            if s[i] == '0':
                s[i] = '1'
                c = '0'
                break
            else:
                s[i] = '0'
        
        if c == '1':
            s.append('1')
        
        s.reverse()  # Reverse back to original order
        
        # Convert list back to string
        result = ''.join(s)
        
        # Trim leading zeros
        i = 0
        while i < len(result) and result[i] == '0':
            i += 1
        
        return result[i:] if i < len(result) else '0'
