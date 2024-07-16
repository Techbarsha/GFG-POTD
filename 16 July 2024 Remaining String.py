class Solution:
	def printString(self, s, ch, count):
		# code here
		 # Initialize the counter for occurrences of ch
        occurrence = 0
        # Loop through the string to find the count-th occurrence of ch
        for i in range(len(s)):
            if s[i] == ch:
                occurrence += 1
       # If the count-th occurrence is found, return the remaining substring
                if occurrence == count:
                    return s[i+1:]
        # If count-th occurrence is not found, return an empty string
        return ""
