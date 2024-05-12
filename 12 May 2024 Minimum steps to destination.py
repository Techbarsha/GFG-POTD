class Solution:
    def minSteps(self, d):
        # code here
        # Initialize variables to keep track of steps and cumulative sum
        steps = 0
        cumulative_sum = 0

        # Continue until cumulative_sum reaches or exceeds d, or difference is odd
        while cumulative_sum < d or (cumulative_sum - d) % 2 != 0:
            steps += 1  # Increment steps
            cumulative_sum += steps  # Update cumulative sum

        return steps  # Return the minimum number of steps required to reach d
