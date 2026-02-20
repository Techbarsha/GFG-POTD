class Solution:
    def inversionCount(self, arr):
        # Code Here
        
        # This code Implemented by Barsha Saha
        
        def merge_sort(arr, temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                # Count inversions in left half
                inv_count += merge_sort(arr, temp, left, mid)

                # Count inversions in right half
                inv_count += merge_sort(arr, temp, mid + 1, right)

                # Count split inversions
                inv_count += merge(arr, temp, left, mid, right)

            return inv_count

        # Merge function
        def merge(arr, temp, left, mid, right):
            i = left       
            j = mid + 1   
            k = left      
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)  
                    j += 1
                k += 1
          
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            # Copy sorted subarray back to original array
            for idx in range(left, right + 1):
                arr[idx] = temp[idx]

            return inv_count

        n = len(arr)
        temp = [0] * n
        return merge_sort(arr, temp, 0, n - 1)
