class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code edutech barsha
        # Initialize pointers and variables
        i, j = 0, 0
        sum1, sum2 = 0, 0
        max_sum = 0

        # Traverse through both arrays
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:  # arr1[i] == arr2[j]
                max_sum += max(sum1, sum2) + arr1[i]
                sum1, sum2 = 0, 0
                i += 1
                j += 1
        
        # Add remaining elements of arr1, if any
        while i < len(arr1):
            sum1 += arr1[i]
            i += 1
        
        # Add remaining elements of arr2, if any
        while j < len(arr2):
            sum2 += arr2[j]
            j += 1
        
        # Final update of max_sum
        max_sum += max(sum1, sum2)
        
        return max_sum
