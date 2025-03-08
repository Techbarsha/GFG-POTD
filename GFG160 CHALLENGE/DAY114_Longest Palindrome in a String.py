class Solution:
    def longestPalindrome(self, s):
        # code here
        res=""
        ma=0
        
        for i in range(len(s)):
            l=i
            r=i
            while l >= 0 and r<len(s) and s[l]==s[r]:
                if r-l+1>ma:
                    ma=r-l+1
                    res=s[l:l+r-l+1]
                l-=1
                r+=1
            l=i
            r=l+1
            while l>= 0 and r<len(s) and s[l]==s[r]:
                if r-l+1>ma:
                    ma=r-l+1
                    res=s[l:l+r-l+1]
                l-=1
                r+=1
        return res
