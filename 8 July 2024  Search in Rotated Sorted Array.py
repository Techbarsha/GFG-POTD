class Solution:
    def search(self,arr,key):
        # Complete this function
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # If the key is found
            if arr[mid] == key:
                return mid
            
            # Check if the left half is sorted
            if arr[low] <= arr[mid]:
                # Check if the key lies in the left half
                if arr[low] <= key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if the key lies in the right half
                if arr[mid] < key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        # If the key is not found
        return -1
