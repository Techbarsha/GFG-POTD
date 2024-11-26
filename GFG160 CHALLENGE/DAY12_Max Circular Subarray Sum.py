def circularSubarraySum(arr):
    ##Your code here
    n = len(arr)
    maxSum = float('-inf')
    minSum = float('inf')
    s1 = 0 
    s2 = 0 
    TotalSum = 0

    for num in arr:
        TotalSum += num
        s1 += num
        if s1 < 0:
            s1 = 0
            
        maxSum = max(maxSum, s1)
        s2 += num
        if s2 > 0:
            s2 = 0
            
        minSum = min(minSum, s2)

    if maxSum < 0:
        return maxSum

    return max(maxSum, TotalSum - minSum)
