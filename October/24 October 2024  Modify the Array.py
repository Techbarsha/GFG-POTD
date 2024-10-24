class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n = len(arr)
        
        # First pass: Modify the array based on the condition
        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] *= 2   # Double the current element
                arr[i + 1] = 0  # Set the next element to 0

        # Second pass: Move non-zero elements to the front
        result = []
        count_zeros = 0

        for num in arr:
            if num != 0:
                result.append(num)
            else:
                count_zeros += 1

        # Add the zeros at the end
        result.extend([0] * count_zeros)

        return result
