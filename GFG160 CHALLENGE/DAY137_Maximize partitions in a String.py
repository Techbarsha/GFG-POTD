class Solution:
    def maxPartitions(self , s: str) -> int:
        # code here
        last_index={ch:i for i,ch in enumerate(s)}
        ans,ind = 0,0
        for i,ch in enumerate(s):
            ind = max(ind,last_index[ch])
            if ind == i:
                ans += 1
        return ans    
