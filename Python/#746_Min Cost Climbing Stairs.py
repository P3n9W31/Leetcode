class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f = cost
        for i in range(len(f)-3,-1,-1):
            f[i] = cost[i] + min(f[i+1], f[i+2])
        return min(f[0],f[1])