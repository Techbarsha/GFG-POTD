class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()  # Step 1: Sort the array
        n = len(arr)
        closest_sum = float('inf')  # Initialize the closest sum to infinity

        for i in range(n - 2):  # Iterate through the array, fixing one element at a time
            left, right = i + 1, n - 1  # Initialize two pointers

            while left < right:  # While the two pointers do not cross
                current_sum = arr[i] + arr[left] + arr[right]  # Calculate the sum of the triplet

                if current_sum == target:  # If the current sum is exactly the target, return it
                    return current_sum

                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target) or \
                   (abs(current_sum - target) == abs(closest_sum - target) and current_sum > closest_sum):
                    closest_sum = current_sum

                # Move the pointers based on the comparison of current sum and target
                if current_sum < target:
                    left += 1  # Move the left pointer to the right to increase the sum
                else:
                    right -= 1  # Move the right pointer to the left to decrease the sum
        
        return closest_sum  # Return the closest sum found
