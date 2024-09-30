from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        # Calculate the difference and sort based on the absolute value of the difference
        orders = sorted(range(n), key=lambda k: abs(arr[k] - brr[k]), reverse=True)
        
        totalTips = 0
        countA = 0
        countB = 0
        
        for i in orders:
            if (countA < x and arr[i] >= brr[i]) or countB >= y:
                totalTips += arr[i]
                countA += 1
            else:
                totalTips += brr[i]
                countB += 1
                
        return totalTips
