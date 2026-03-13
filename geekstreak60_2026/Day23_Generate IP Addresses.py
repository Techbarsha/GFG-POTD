class Solution:
    def generateIp(self, s):
        # Code here
        
        # This code implemented by Barsha Saha
        res = []
        n = len(s)

        # Function to check if segment is valid
        def is_valid(part):
            if len(part) > 1 and part[0] == '0':
                return False
            return int(part) <= 255

        # Try all combinations
        for i in range(1, min(4, n)):
            for j in range(i+1, i + min(4, n-i)):
                for k in range(j+1, j + min(4, n-j)):
                    if k < n:
                        a = s[:i]
                        b = s[i:j]
                        c = s[j:k]
                        d = s[k:]

                        if is_valid(a) and is_valid(b) and is_valid(c) and is_valid(d):
                            res.append(a + "." + b + "." + c + "." + d)

        return res
        
        
