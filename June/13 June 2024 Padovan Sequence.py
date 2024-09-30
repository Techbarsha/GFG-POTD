class Solution:
    def padovanSequence(self, n):
        # code here 
        MOD = 10**9 + 7
        
        if n == 0 or n == 1 or n == 2:
            return 1
        
        p0, p1, p2 = 1, 1, 1
        for i in range(3, n + 1):
            p_next = (p0 + p1) % MOD
            p0, p1, p2 = p1, p2, p_next
        
        return p2
