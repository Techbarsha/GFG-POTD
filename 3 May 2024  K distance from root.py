class Solution:
    def KDistance(self, root, k):
        result = []
        self.printKDistance(root, k, result)
        return result
    
    def printKDistance(self, root, k, result):
        if root is None:
            return
        if k == 0:
            result.append(root.data)
        else:
            self.printKDistance(root.left, k - 1, result)
            self.printKDistance(root.right, k - 1, result)
