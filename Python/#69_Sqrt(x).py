class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        from math import floor
        return floor(x**0.5)