class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        x = str(x)
        if x[0] == '-':
            neg = True
        if neg:
            x = int(x[:0:-1]) * -1
        else:
            x = int(x[::-1])
        if x > 2**31 or x <= -(2**31):
            return 0
        return x