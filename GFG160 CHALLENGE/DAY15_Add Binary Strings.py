class Solution:
	def addBinary(self, s1, s2):
		# code here
		result = ''
        carry = 0
        max_l = max(len(s1), len(s2))
        s1 = s1.zfill(max_l)
        s2 = s2.zfill(max_l)
        for i in range(max_l - 1, -1, -1):
            bsum = carry
            bsum += 1 if s1[i] == '1' else 0
            bsum += 1 if s2[i] == '1' else 0
            result = ('1' if bsum % 2 == 1 else '0') + result
            carry = 0 if bsum < 2 else 1
        if carry != 0:
            result = '1' + result
        return result.lstrip('0') or '0'
