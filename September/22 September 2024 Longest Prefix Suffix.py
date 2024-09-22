class Solution:
	def lps(self, str):
		# code edutech barsha
		n = len(str)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if str[i] == str[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                   
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps[-1]
