class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        alist = [1,1]
        for i in range(n-1):
            alist.append(alist[i]+alist[i+1])
        return alist[-1]