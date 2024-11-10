class Solution:
    def findUnion(self, a, b):
        result = []
        i, j = 0, 0
        
        # Traverse both arrays
        while i < len(a) and j < len(b):
            # If element in a is smaller, add it
            if a[i] < b[j]:
                if not result or result[-1] != a[i]:  # Check for duplicates
                    result.append(a[i])
                i += 1
            # If element in b is smaller, add it
            elif a[i] > b[j]:
                if not result or result[-1] != b[j]:  # Check for duplicates
                    result.append(b[j])
                j += 1
            # If both are equal, add one of them
            else:
                if not result or result[-1] != a[i]:  # Check for duplicates
                    result.append(a[i])
                i += 1
                j += 1
        
        # Add remaining elements from a
        while i < len(a):
            if not result or result[-1] != a[i]:  # Check for duplicates
                result.append(a[i])
            i += 1

        # Add remaining elements from b
        while j < len(b):
            if not result or result[-1] != b[j]:  # Check for duplicates
                result.append(b[j])
            j += 1
        
        return result
