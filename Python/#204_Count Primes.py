class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        res = [1] * n
        res[0],res[1] = 0,0
        for i in range(2, int(n ** 0.5) + 1):
            if res[i] == 1:
                res[i * i:n:i] = [0] * int((n-i*i-1)/i + 1)
        return sum(res)      