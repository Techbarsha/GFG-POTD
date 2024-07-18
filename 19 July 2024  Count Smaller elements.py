class Solution:

	def mergeSort(self, enum):
        half = len(enum) // 2
        if half:
            left, right = self.mergeSort(enum[:half]), self.mergeSort(enum[half:])
            for i in range(len(enum) - 1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]:
                    self.smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
	
	
	
	def constructLowerArray(self,arr):
		# code here
		self.smaller = [0] * len(arr)
        self.mergeSort(list(enumerate(arr)))
        return self.smaller
