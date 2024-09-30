class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        S_n = n * (n + 1) // 2 
        SS_n = n * (n + 1) * (2 * n + 1) // 6  
        
        S_arr = sum(arr)
        SS_arr = sum(x * x for x in arr)
        
        diff_sum = S_n - S_arr  
        diff_square_sum = SS_n - SS_arr  
        
        sum_ab = diff_square_sum // diff_sum
        
        A = (diff_sum + sum_ab) // 2
        B = A - diff_sum
        
        return [B, A]
