class Solution:
    def wordBreak(self, s: str, dictionary: list[str]) -> bool:
        # code here
        word_set = set(dictionary)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        max_len=0
        if dictionary:
            max_len=max(len(word) for word in dictionary)
        for i in range(1,n+1):
            for j in range(max(0,i-max_len),i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]=True
                    break
        return dp[n] 
