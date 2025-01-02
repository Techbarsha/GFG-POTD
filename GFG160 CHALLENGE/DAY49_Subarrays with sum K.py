#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        cum_sum_count = {0: 1}
        cum_sum = 0
        count = 0
        
        for num in arr:
            cum_sum += num
            
            if (cum_sum - k) in cum_sum_count:
                count += cum_sum_count[cum_sum - k]
                
            cum_sum_count[cum_sum] = cum_sum_count.get(cum_sum, 0) + 1   
            
        return count 
