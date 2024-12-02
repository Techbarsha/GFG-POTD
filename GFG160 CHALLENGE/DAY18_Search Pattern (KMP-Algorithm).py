class Solution:
    def search(self, pat, txt):
        # code here
        result = []
        m = len(pat)
        n = len(txt)
        for i in range(n - m + 1):
            if txt[i:i + m] == pat:
                result.append(i)
        
        return result
