class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
