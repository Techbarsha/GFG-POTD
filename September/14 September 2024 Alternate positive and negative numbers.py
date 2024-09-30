class Solution:
    def rearrange(self,arr):
        # code edutech barsha
        pos = []  
        neg = []  
        # Separate positive and negative numbers
        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        # Merge them in alternate order
        # Pointers for pos, neg, and the result array
        i = j = k = 0  
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            i += 1
            if k < len(arr):
                arr[k] = neg[j]
                k += 1
                j += 1
        # Append remaining elements from positive or negative array
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1
        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1
