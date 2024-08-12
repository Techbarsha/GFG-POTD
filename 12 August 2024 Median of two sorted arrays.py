class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code edutech barsha
        i = j = 0
        n = len(arr1)
        merged = []
        
        while i < n and j < n:
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        while i < n:
            merged.append(arr1[i])
            i += 1
        
        while j < n:
            merged.append(arr2[j])
            j += 1
        
        return merged[n-1] + merged[n]
