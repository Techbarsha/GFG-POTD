class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        # Binary search to find the closest position to x
        low, high = 0, n - 1
        mid = 0
        mn = float('inf')  # Initialize the minimum difference to infinity
        ans = -1  # Initialize the index of the closest element

        # Binary search to find the closest element to x
        while low <= high:
            mid = (low + high) // 2
            diff = abs(arr[mid] - x)

            # Update the closest position if a closer element is found
            if diff <= mn:
                if ans == -1:
                    ans = mid
                else:
                    if diff == mn and arr[ans] < arr[mid]:
                        ans = mid
                    if diff < mn:
                        ans = mid
                mn = diff

            # Adjust the search range based on comparison
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        vec = []
        total = 0
        i, j = ans - 1, ans + 1

        # If the closest element is not x itself, add it to the result
        if arr[ans] != x:
            vec.append(arr[ans])
            total += 1

        # Collect k closest elements using two pointers
        while total < k:
            if i >= 0 and j < n:
                # Compare the differences from x and add the closer element
                if abs(arr[i] - x) < abs(arr[j] - x):
                    vec.append(arr[i])
                    i -= 1
                else:
                    vec.append(arr[j])
                    j += 1
            elif i >= 0:
                # If only elements on the left are available
                vec.append(arr[i])
                i -= 1
            else:
                # If only elements on the right are available
                vec.append(arr[j])
                j += 1
            total += 1

        return vec
