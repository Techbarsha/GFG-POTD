class Solution:
    def minRow(self,n,m,a):
        #code here
        min_ones_count = math.inf
        min_row_index = -1
        
        for i in range(n):
            ones_count = sum(a[i])
            if ones_count < min_ones_count:
                min_ones_count = ones_count
                min_row_index = i
                
        return min_row_index + 1
