class Solution:
    def roundToNearest(self, str_num: str) -> str:
        #Complete the function
        str_num = list(str_num)
        n = len(str_num)

        if str_num[n-1] <= '5':
            str_num[n-1] = '0'
            return ''.join(str_num)
        
        str_num[n-1] = '0'
        i = n - 2
        
        while i >= 0 and str_num[i] == '9':
            str_num[i] = '0'
            i -= 1
        
        if i < 0:
            str_num.insert(0, '1')
        else:
            str_num[i] = chr(ord(str_num[i]) + 1)

        return ''.join(str_num)
