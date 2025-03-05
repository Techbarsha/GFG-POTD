class Solution:
    def longestStringChain(self, words):
        # Code here
        max_len = 1
        dp={}
        words.sort(key=len)
        for word in words:
            dp[word]=1
            words.sort(key=len)
            for word in words:
                dp[word]=1
                for i in range(len(word)):
                    pred=word[:i]+word[i+1:]
                    if pred in dp:
                        dp[word]=max(dp[word],1+dp[pred])
                max_len=max(max_len,dp[word])
            return max_len
