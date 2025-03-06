class Solution:
    def lcs(self, s1: str, s2: str) -> int:
        # code here
        m,n = len(s1), len(s2)
        subs = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    subs[i][j] = subs[i-1][j-1]+1
                else:
                    subs[i][j] = max(subs[i-1][j],subs[i][j-1])
        return subs[m][n]
