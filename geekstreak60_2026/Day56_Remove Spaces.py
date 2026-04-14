class Solution:
    def removeSpaces(self, s):
        # code here
        # This code implemented by Barsha Saha
        result = ""
        for ch in s:
            if ch != " ":
                result += ch
        return result
        
