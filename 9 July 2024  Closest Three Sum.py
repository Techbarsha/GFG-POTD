class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()
        n = len(arr)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(closest_sum - target) or (abs(current_sum - target) == abs(closest_sum - target) and current_sum > closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
