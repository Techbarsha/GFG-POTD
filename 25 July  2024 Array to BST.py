class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        # code here
        if not nums:
            return None
        
        return self._sortedArrayToBST(nums, 0, len(nums) - 1)
    
    def _sortedArrayToBST(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = Node(nums[mid])
        node.left = self._sortedArrayToBST(nums, left, mid - 1)
        node.right = self._sortedArrayToBST(nums, mid + 1, right)
        
        return node
