class Solution:
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.data)
            self.inorder(root.right, res)
    
    def merge_sorted_arrays(self, arr1, arr2):
        merged = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
        
        return merged

    def merge(self, root1, root2):
        # code here
        res1 = []
        res2 = []
        self.inorder(root1, res1)
        self.inorder(root2, res2)
        
        return self.merge_sorted_arrays(res1, res2)
