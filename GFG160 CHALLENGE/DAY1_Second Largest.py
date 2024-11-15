class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = second_largest = None
        
        for num in arr:
            if largest is None or num > largest:
                second_largest = largest
                largest = num
            elif num != largest and (second_largest is None or num > second_largest):
                second_largest = num
        
        return second_largest if second_largest is not None else -1
