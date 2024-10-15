class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        prefix_sum_freq = {}
        prefix_sum_freq[0] = 1  
        current_sum = 0
        count = 0
        
        for num in arr:
            current_sum += num
            if (current_sum - tar) in prefix_sum_freq:
                count += prefix_sum_freq[current_sum - tar]
            if current_sum in prefix_sum_freq:
                prefix_sum_freq[current_sum] += 1
            else:
                prefix_sum_freq[current_sum] = 1
