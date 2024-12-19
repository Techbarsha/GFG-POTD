#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        # Initialize a variable to keep track of the last number
        prev = 0
        missing_count = 0

        # Traverse through the array
        for num in arr:
            missing_in_range = num - prev - 1
            if missing_count + missing_in_range >= k:
                return prev + (k - missing_count)
            missing_count += missing_in_range
            prev = num  

        return prev + (k - missing_count)
